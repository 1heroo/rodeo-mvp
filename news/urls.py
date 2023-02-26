from django.urls import path

from news.views import NewsListView


urlpatterns = [
    path('news/', NewsListView.as_view())
]