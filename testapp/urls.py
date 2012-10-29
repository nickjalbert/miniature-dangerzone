from django.conf.urls import patterns, include, url
from testapp.views import home


urlpatterns = patterns('',
        url(r'$', home),
)
