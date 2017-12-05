from rest_framework import serializers
from ticket.models import Ticket
 
class TicketSerializer(serializers.HyperlinkedModelSerializer):
    
    def create(self, validated_data):
        ticket = Ticket(
            userid=validated_data.get('userid', None),
            contains=validated_data.get('contains', None),
        )
        ticket.save()
        return ticket
 
    class Meta:
        model = Ticket
        fields = ('url', 'id', 'tickettime',
                  'userid', 'contains'
                  )
        extra_kwargs = {
            'url': {
                'view_name': 'ticket:ticket-detail',
            }
        }
        