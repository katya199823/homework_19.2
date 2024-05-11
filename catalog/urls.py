from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactDetailView, GameDetailView, GenresListView, GameCreateView, \
    GameUpdateView, BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, GameDeleteView

app_name = CatalogConfig.name




urlpatterns = [
                  path('', HomeListView.as_view(), name='games_list'),
                  path('contacts/', ContactDetailView.as_view(), name='contacts'),
                  path('genres_list/', GameDetailView.as_view(), name='genres'),
                  path('<int:pk>/game_detail/', GenresListView.as_view(), name='game_detail'),

                  path('create/', GameCreateView.as_view(), name='game_create'),
                  path('update/<int:pk>/', GameUpdateView.as_view(), name='game_update'),
                  path('delete/<int:pk>/', GameDeleteView.as_view(), name='game_delete'),

                  path('blog/', BlogListView.as_view(), name='blog_list'),
                  path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
                  path('blog/detail/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
                  path('blog/update/<slug:slug>/', BlogUpdateView.as_view(), name='blog_update'),
                  path('blog/delete/<slug:slug>/', BlogDeleteView.as_view(), name='blog_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
