from django.shortcuts import render
from rest_framework.generics import ListAPIView

from news.serializers import NewsSerializer
from news.models import News
from rodeo_kg.pagination import StandardResultsSetPagination


# Create your views here.


class NewsListView(ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return News.objects.all()

