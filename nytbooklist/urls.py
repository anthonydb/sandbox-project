from django.urls import path
from nytbooklist.views import BookListFictionView, BookListNonfictionView, BooklistHomeView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('fiction/', BookListFictionView, name='fiction_list'),
    path('nonfiction/', BookListNonfictionView, name='non_fiction_list'),
    path('', BooklistHomeView.as_view(), name='booklist_home')
]
