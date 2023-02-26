from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from rodeo_kg.pagination import StandardResultsSetPagination
from .models import Tournament, Champion, Gallery
from .serializers import TournamentSerializer, ChampionSerializer, GallerySerializer


class TournamentModelViewSet(ModelViewSet):

    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = [IsAuthenticated]


class ChampionListView(ListAPIView):
    serializer_class = ChampionSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Champion.objects.all()


class GalleryListView(ListAPIView):
    serializer_class = GallerySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Gallery.objects.all()
