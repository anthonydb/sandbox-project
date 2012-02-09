#from random import randint
from django.db import models
#from django.db.models import Count, Max

#this is a test of using a model manager
#to pull a random quote

#class QuoteManager(models.Manager):
#    def pull_random_quote(self):
#        count = self.all().aggregate(count=Count('id'))['count']
#        random_index = randint(0, count -1)
#        return self.all()[random_index]            
#
#    def random_naive(self):
#        return self.all().order_by('?')[0]
#
#    def test(self):
#        return self.all()[3]

class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    displayname = models.CharField(max_length=200)
    brfbio = models.CharField('Brief bio', max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['lastname']

    def __unicode__(self):
        return self.displayname

    @models.permalink
    def get_absolute_url(self):
        return ('author_quotes', (), { 'authorslug': self.slug })

class Categories(models.Model):
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['category']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.category

    @models.permalink
    def get_absolute_url(self):
        return ('category_quotes', (), { 'categoryslug': self.slug })

class Quote(models.Model):
    quote = models.TextField()
    source = models.CharField(max_length=400)
    author = models.ForeignKey(Author)
    categories = models.ManyToManyField(Categories)
    slug = models.SlugField(unique=True)
    #objects = models.Manager()
    #random = QuoteManager()

    def __unicode__(self):
        return self.quote

    @models.permalink
    def get_absolute_url(self):
        return ('quote_detail', (), { 'quoteslug': self.slug })
    
class Submission(models.Model):
    item = models.TextField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)
    source = models.TextField()

    class Meta:
        ordering = ['item']
        verbose_name_plural = 'Submissions'

    def __unicode__(self):
        return self.item
