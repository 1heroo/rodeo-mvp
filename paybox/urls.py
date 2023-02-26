from django.urls import path

from paybox.views import TicketListView

urlpatterns = [
    path('tickets/', TicketListView.as_view())
]