from django.conf.urls import url, include


urlpatterns = [
    url('^api/', include('socnetapi.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
]
