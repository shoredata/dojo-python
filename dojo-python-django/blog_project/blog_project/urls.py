"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# #################################
# DEFAULT FROIM DJANGO:
# #################################
# from django.contrib import admin
# from django.urls import path
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# blogs app
# ---------
# /blogs        - display "placeholder to later display all the list of blogs" via HttpResponse. 
#                 Have this be handled by a method named 'index'.
# /blogs/new    - display "placeholder to display a new form to create a new blog" via HttpResponse. 
#                 Have this be handled by a method named 'new'.
# /blogs/create - Have this be handled by a method named 'create'.  
#                 For now, have this url redirect to /blogs.
# /blogs/{{number}} - display 'placeholder to display blog {{number}}.  
#                     For example /blogs/15 should display a message 'placeholder to display blog 15'.  
#                     Have this be handled by a method named 'show'.
# /blogs/{{number}}/edit - display 'placeholder to edit blog {{number}}.  
#                           Have this be handled by a method named 'edit'.
# /blogs/{{number}}/delete - Have this be handled by a method named 'destroy'. 
#                           For now, have this url redirect to /blogs. 

# surveys app
# -----------
# /surveys       - display "placeholder to display all the surveys created"
# /surveys/new   - display "placeholder for users to add a new survey

# users app
# ---------
# /register   - display 'placeholder for users to create a new user record'
# /login      - display 'placeholder for users to login' 
# /users/new  - have the same method that handles /register also handle the url request of /users/new
# /users - display 'placeholder to later display all the list of users'

# Have the root route (e.g. localhost/) be handled by the index method in the blogs' view file.

from django.conf.urls import url, include
urlpatterns = [
    url(r'^random_word/', include('apps.random_word.urls')),
    url(r'^blogs/', include('apps.blogs.urls')),
    url(r'^surveys/', include('apps.surveys.urls')),
    url(r'^users/', include('apps.users.urls')),
    url(r'^test/', include('apps.blog_app1.urls')),
    url(r'^', include('apps.blogs.urls')), # catches register/ and login/
]

