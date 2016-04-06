from django.conf.urls import url
from core.views import HomePageView
from django.conf import settings  # remove for production
from django.conf.urls.static import static  # remove for production

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
