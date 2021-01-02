from django.db import models
from django.contrib.auth.models import User

""""
Major Class: designates the major(s) of an editor
"""


class Major(models.Model):
    lst = ['Computer Science', 'Business', 'Finance', 'Economics', 'Nursing', 'Communications', 'Philosophy',
           'Political Science', 'Psychology', 'Biology', 'Pre-Medicine', 'English', 'Electrical Engineering',
           'Physics', 'Chemistry', 'Mechanical Engineering', 'Biomedical Engineering', 'Math', 'History',
           'Environmental Studies', 'Education', 'Sociology', 'Journalism', 'Fine Arts']
    majors = sorted(lst)  # sort majors alphabetically
    CHOICES = [(major, major) for major in majors]

    name = models.CharField(choices=CHOICES, max_length=100)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


""""
School Class: designates the school(s) an editor got into
"""


class School(models.Model):
    lst = ['Harvard', 'Yale', 'Princeton', 'Stanford', 'MIT', 'Columbia', 'UPenn', 'Dartmouth',
           'Cornell', 'Brown', 'UC Berkeley', 'UT Austin', 'UMich', 'UChicago', 'Duke',
           'Northwestern', 'John\'s Hopkins', 'New York University', 'Caltech', 'Carnegie Mellon',
           'Georgia Tech', 'University of Southern California', 'UCLA', 'UIUC', 'UC San Diego',
           'University of Washington', 'Washington University (St. Louis)']
    colleges = sorted(lst)  # sort colleges alphabetically
    CHOICES = [(college, college) for college in colleges]

    name = models.CharField(choices=CHOICES, max_length=100)
    follower = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


"""
Editor class: core model to be displayed, has a name, bio, associated colleges, associated majors, and a photo
"""


class Editor(models.Model):
    editor_name = models.CharField(max_length=25)
    bio = models.TextField()
    college = models.ManyToManyField(School)
    major = models.ManyToManyField(Major)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.editor_name

    # Get colleges associated with the Editor
    def colleges(self):
        return School.objects.filter(editor=Editor.objects.get(editor_name=self.editor_name))

    # Get majors associated with the Editor
    def majors(self):
        return Major.objects.filter(editor=Editor.objects.get(editor_name=self.editor_name))



"""
Follow class: models a follow relationship between an editor object and a user
"""
class Follow(models.Model):
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, on_delete=models.CASCADE)


"""
Request class: models an essay edit request between an editor object and a user
"""
class Request(models.Model):
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, on_delete=models.CASCADE)
