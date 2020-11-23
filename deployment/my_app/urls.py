from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from .views import *

from deployment import settings

urlpatterns = [
                # Django URLS
                path('', views.home, name = 'home'),



                # Rest URLS
                path('predict', PredictAPIView.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)