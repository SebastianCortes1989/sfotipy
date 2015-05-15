from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from albums.views import AlbumDetailView
from rest_framework import routers
from albums.views import AlbumViewSet
from userprofiles.views import LoginView
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'albums', AlbumViewSet, 'Album')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^negocio/(?P<slug>[-\w]+)/$', mi_vista, name='mi_vista')
    url(r'^tracks/(?P<title>[\w\-]+)', 'tracks.views.tracks_view', name='tracks_view'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
    url(r'^albums/(?P<pk>[\d]+)', AlbumDetailView.as_view()),
    url(r'^login/$', LoginView.as_view(), name='login'),    
    url(r'^logint/$', TemplateView.as_view(template_name='signup.html'), name='login'),
    url(r'^api/', include(router.urls, namespace="api")),
)
