from django.shortcuts import render
from rest_framework.generics import ListAPIView

from paybox.models import Ticket
from paybox.serializers import TicketSerializer
from rodeo_kg.pagination import StandardResultsSetPagination


class TicketListView(ListAPIView):
    serializer_class = TicketSerializer
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Ticket.objects.all()
