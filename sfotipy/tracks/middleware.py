
from django.http import HttpResponse

class PaisMiddleware():
	
	def process_request(self, request):
		pais = 'Chile'
		return HttpResponse(pais)
