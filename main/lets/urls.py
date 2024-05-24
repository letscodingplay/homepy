from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static 

from . import views

app_name = 'lets'

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("intro", views.Intro.as_view(), name="intro"),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
