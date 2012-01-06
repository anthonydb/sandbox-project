from anthonydb.quotes.models import Author, Categories, Quote, Submission
from django.contrib import admin

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('item', 'source', 'name', 'email', 'date') 

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("displayname",)}

class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category",)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Quote)
admin.site.register(Submission, SubmissionAdmin)

