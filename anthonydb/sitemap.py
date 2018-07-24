from django.contrib.sitemaps import Sitemap, GenericSitemap
from django.urls import reverse
from quotes.models import Author, Categories, Quote

author_dict = {
    'queryset': Author.objects.all()
}
category_dict = {
    'queryset': Categories.objects.all()
}
quote_dict = {
    'queryset': Quote.objects.all(),
    'date_field': 'create_date'
}


class ViewSitemap(Sitemap):
    """Reverse static views for XML sitemap."""
    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home', 'about', 'suggest', 'apihome', 'books']

    def location(self, item):
        return reverse(item)


sitemaps = {
    'author': GenericSitemap(author_dict, priority=0.6),
    'categories': GenericSitemap(category_dict, priority=0.6),
    'quotes': GenericSitemap(quote_dict, priority=0.8),
    'views': ViewSitemap
}
