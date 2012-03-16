import settings
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns(
    'reporting.views',
    url(r'^home/?$', 'home', name='home'),
    url(r'^report/?$', 'report', name='report'),
    url(r'^add_status_value/?$', 'add_status_value', name='add_status_value'),
    url(r'^new_status_value/?$', 'new_status_value', name='new_status_value')
)
