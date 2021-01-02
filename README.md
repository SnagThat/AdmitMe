# CIS192 Final Project: Startup Website
Sahitya Senapathy
CIS 192, Fall 2020

## Concept
For my final project, I made a website for my startup AdmitMe, a platform connecting
college students to high school seniors who want to get essay editing for 
their college applications. This website is designed to allow an ordinary user
to find a good match and connect with them by email.

## Important Note

The email sending feature as you see in the demo video uses my email credentials, which were 
in settings.py. I have removed them from the submission for privacy. The code may not work unless you put
in a valid gmail account and password (and allow access to non-Google apps in security).

## Submission Requirements
1. One Class Definition:
    - main.models.py includes the following classes: Major, School, Editor, Follow, Request
    - Major class in main.models.py contains two magic methods
2. Two non-trivial first-party packages
    - random is used to generate an ID code that is sent to the user's email for every essay edit they request
    - os is used in settings.py to manage files
3. Two non-trivial third-party packages
    - Django
    - Pillow (for images)
4. In-line documentation

## Website Structure
- Landing page:
  - route: '/'
- Account Registration page:
    - route: '/register'
- Platform page:
    - route: '/platform'
- Filtered results:
    - route: '/filtered/(college name)'
- Editor page:
    - route: '/editor?id=(editor id)'
- User profile page:
    - route: '/profile'