"""survey_form URL Configuration

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
from django.conf.urls import url, include
urlpatterns = [
    # url(r'^surveys/', include('apps.random_word.urls')),
    # url(r'^blogs/', include('apps.blogs.urls')),
    # url(r'^surveys/', include('apps.surveys.urls')),
    # url(r'^users/', include('apps.users.urls')),
    # url(r'^test/', include('apps.blog_app1.urls')),
    url(r'^session_words/', include('apps.session_words.urls')),
    url(r'^', include('apps.surveys.urls')), # catches everything else
]

