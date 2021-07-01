from rest_framework import serializers
from .models import storeEvent

# EVENT SERIALIZERS
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = storeEvent
        fields = '__all__'

