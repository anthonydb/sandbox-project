from django.contrib import admin
from sotu.models import Speech


class SpeechAdmin(admin.ModelAdmin):
    list_display = ('president', 'title', 'speech_date')
    readonly_fields = ('president', 'title', 'speech_date', 'speech_text', 'search_speech_text')

admin.site.register(Speech, SpeechAdmin)