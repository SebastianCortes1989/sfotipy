from django.contrib import admin

from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('title', 'number', 'album_id')
	list_filter = ('title', 'album_id')
	search_fields = ('title', 'album_id__title')

# Register your models here.
admin.site.register(Track, TrackAdmin)