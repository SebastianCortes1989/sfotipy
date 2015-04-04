from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	#url(r'^negocio/(?P<slug>[-\w]+)/$', mi_vista, name='mi_vista')
    url(r'^tracks/(?P<title>[\w\-]+)', 'tracks.views.tracks_view', name='tracks_view'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
)
