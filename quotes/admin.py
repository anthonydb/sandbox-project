from quotes.models import Author, Categories, Quote, Submission
from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("display_name",)}
    list_display = ('display_name', 'brief_bio', 'first_name', 'last_name')


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category",)}


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'create_date')


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('item', 'source', 'name', 'email', 'date', 'ip_address', 'misc_headers')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Submission, SubmissionAdmin)
