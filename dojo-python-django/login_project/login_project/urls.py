from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.login_app.urls')), # catches all
    # url(r'^', include('apps.users_app.urls')), # catches all
]
