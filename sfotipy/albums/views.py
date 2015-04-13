from django.shortcuts import render
from django.views.generic.detail import DetailView
from albums.models import Album

# Create your views here.
class AlbumDetailView(DetailView):
	model = Album
	context_object_name = 'albums'
	template_name = "album.html"
	