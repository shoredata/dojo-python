from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.courses_app.urls')), # catches all
]
