from django.urls import path, include
from rest_framework import routers

from tournaments.views import TournamentModelViewSet, ListAPIView, ChampionListView, GalleryListView

# from tournaments.models import TournamentModelViewSet


router = routers.DefaultRouter()
router.register(r'tournament', TournamentModelViewSet, basename='tournament')


urlpatterns = [
    path('', include(router.urls)),
    path('champions/', ChampionListView.as_view()),
    path('gallery/', GalleryListView.as_view()),
]