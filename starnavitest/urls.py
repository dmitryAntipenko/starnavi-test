from django.conf.urls import url, include


urlpatterns = [
    url('^', include('socnetapi.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
