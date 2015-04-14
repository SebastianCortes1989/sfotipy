from django.shortcuts import render
from django.views.generic.detail import DetailView
from albums.models import Album
from albums.serializers import AlbumSerializer


# Create your views here.
class AlbumDetailView(DetailView):
	model = Album
	context_object_name = 'albums'
	template_name = "album.html"
	
from rest_framework import viewsets


class AlbumViewSet(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer
