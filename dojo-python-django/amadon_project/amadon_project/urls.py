from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.amadon_app.urls')), # catches all
]
