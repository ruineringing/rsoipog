from ticket.models import Ticket
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from ticket.serializers import TicketSerializer
 
class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
 
class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
 
    def get_queryset(self):
        return Ticket.objects.all().filter(id=self.kwargs['pk'])