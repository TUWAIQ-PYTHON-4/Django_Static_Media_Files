from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'PMApp'

urlpatterns = [
                  path('', views.project_list, name='project_list'),
                  # path('about/', views.about, name='about'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
