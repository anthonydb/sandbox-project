from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

class Speech(models.Model):
    president = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    speech_date = models.DateField()
    speech_text = models.TextField()
    search_speech_text = SearchVectorField(null=True)

    class Meta:
        ordering = ['speech_date']
        verbose_name_plural = 'Speeches'
        indexes = [
            GinIndex(fields=['search_speech_text'])
        ]
