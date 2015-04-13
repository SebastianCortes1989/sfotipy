from django.contrib import admin

from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('title', 'number', 'album_id')
	list_filter = ('title', 'album_id')
	list_editable = ('number',)
	search_fields = ('title', 'album_id__title')
	raw_id_field = ('album_id',)
	#actions = ()

# Register your models here.
admin.site.register(Track, TrackAdmin)