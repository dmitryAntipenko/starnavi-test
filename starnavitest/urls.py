from django.conf.urls import url, include


urlpatterns = [
    url(r'^api/', include('socnetapi.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
]
