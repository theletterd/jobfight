import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = patterns(
    '',

    # Examples:
    # url(r'^$', 'jobfight.views.home', name='home'),
    # url(r'^jobfight/', include('jobfight.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^login/$', auth_views.login, dict(template_name='registration/login.html', extra_context=dict(pagename="Login")), name='auth_login'),
    url(r'^logout/$', auth_views.logout, dict(template_name='registration/logout.html', extra_context=dict(pagename="Logout")), name='auth_logout'),
    url(r'^$', 'reporting.views.home', name='home'),
    url(r'^reporting/', include('reporting.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
