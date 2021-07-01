from .models import storeEvent
from rest_framework import viewsets, permissions
from .serializers import EventSerializer

# EVENT VIEWSET
class EventViewSet(viewsets.ModelViewSet):
    queryset = storeEvent.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EventSerializer

