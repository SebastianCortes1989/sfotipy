from tracks.models import Track

def basico(request):
	tracks = Track.objects.all()

	return {'titulo': 'mi ág', 'tracks': tracks}