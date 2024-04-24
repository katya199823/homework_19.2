from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, genres, game_detail

app_name = CatalogConfig.name

urlpatterns = [
                  path('', home, name='home'),
                  path('contacts/', contacts, name='contacts'),
                  path('genres_list/', genres, name='genres'),
                  path('<int:pk>/game_detail/', game_detail, name='game_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
