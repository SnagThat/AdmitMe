from django.contrib import admin
from django.urls import path
from main.views import main_view, platform_view, register_view, signup_view, login_view, logout_view, editor_view, \
    profile_view, follow_editor_view, follow_college_view, request_editor_view, filtered_view
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import AdmitMe.settings as settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main_view'),
    path('platform', platform_view, name='platform_view'),
    path('filtered/<str:college>', filtered_view, name='filtered_view'),
    path('register', register_view, name='register_view'),
    path('signup/', signup_view, name='signup_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('editor', editor_view, name='editor_view'),
    path('follow', follow_editor_view, name='follow_editor_view'),
    path('request', request_editor_view, name='request_editor_view'),
    path('profile/', profile_view, name='profile_view'),
    path('addcollege/<str:college>', follow_college_view, name='follow_college_view'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)