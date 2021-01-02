from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import School, Editor, Follow, Request
from django.core.mail import EmailMessage
import random
import string


"""
editor_view: returns a profile page of a given editor
"""
def editor_view(request):
    name = request.user.first_name + " " + request.user.last_name
    editor = Editor.objects.get(id=request.GET['id'])
    following_user = User.objects.get(username=request.user.username)

    requested = Request.objects.filter(editor=editor, following_user=following_user).exists()
    following = Follow.objects.filter(editor=editor, following_user=following_user).exists()
    return render(request, 'editor.html',
                  {'editor': editor, 'name': name, 'requested': requested, 'following': following})


"""
follow_college_view: adds the user to a School object's following field
"""
def follow_college_view(request, college):
    college = School.objects.get(name=college)
    following_user = User.objects.get(username=request.user.username)

    college.follower.add(following_user)
    return redirect('/profile/')


"""
follow_editor_view: creates a Follow object with a given Editor object and the User
"""
def follow_editor_view(request):
    editor = Editor.objects.get(id=request.GET['id'])
    following_user = User.objects.get(username=request.user.username)

    if not Follow.objects.filter(editor=editor, following_user=following_user).exists():
        Follow.objects.create(editor=editor, following_user=following_user)

    return redirect('/editor?id=' + str(editor.id))


"""
request_editor_view: creates a Request object with a given Editor object and the User and emails User a standard email
"""
def request_editor_view(request):
    editor = Editor.objects.get(id=request.GET['id'])
    following_user = User.objects.get(username=request.user.username)

    Request.objects.create(editor=editor, following_user=following_user)
    subject = 'AdmitMe: You requested ' + editor.editor_name
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    message = 'Thanks for requesting! Your code is: ' + result_str
    email = EmailMessage(
        subject,
        message,
        to=[request.user.email]
    )
    email.send()

    return redirect('/editor?id=' + str(editor.id))


"""
profile_view: renders the User's profile page with colleges they are following, colleges not followed, editors
followed, and editors requested
"""
def profile_view(request):
    name = request.user.first_name + " " + request.user.last_name
    current_user = User.objects.get(username=request.user)
    colleges = School.objects.filter(follower=current_user)
    other_colleges = School.objects.exclude(follower=current_user)
    follows = Follow.objects.filter(following_user=current_user)
    requests = Request.objects.filter(following_user=current_user)
    return render(request, 'profile.html', {'user': request.user,
                                            'name': name,
                                            'colleges': colleges,
                                            'others': other_colleges,
                                            'follows': follows,
                                            'requests': requests})


"""
filtered_view: renders a page with editors from a certain school
"""
def filtered_view(request, college):
    name = request.user.first_name + " " + request.user.last_name
    school = School.objects.get(name=college)
    editors = Editor.objects.filter(college=school)
    return render(request, 'filtered.html',
                  {'user': request.user, 'name': name, 'editors': editors, 'college': college})


"""
platform_view: renders the main platform with all available editors, as well as a form to allow for filtered search
"""
def platform_view(request):
    if not request.user.is_authenticated:
        return redirect('/register')

    if request.method == 'POST':
        college = request.POST['body']
        if School.objects.filter(name=college).exists():
            return redirect('/filtered/' + college)

    name = request.user.first_name + " " + request.user.last_name
    editors = Editor.objects.all()
    return render(request, 'platform.html', {'user': request.user, 'name': name, 'editors': editors})


"""
login_view: authenticates user login
"""
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/platform')
    else:
        return render('register/error=True')


"""
signup_view: creates new User object
"""
def signup_view(request):
    user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name']
    )

    login(request, user)
    return redirect('/platform')


"""
logout_view: logs user out and redirects to landing page
"""
def logout_view(request):
    logout(request)
    return redirect('/')


"""
register_view: renders user registration page
"""
def register_view(request):
    return render(request, 'register.html', {})


"""
main_view: renders landing page
"""
def main_view(request):
    return render(request, 'main.html', {})
