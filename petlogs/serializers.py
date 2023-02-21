from .models import PetLog
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = PetLog
        # the fields that should be included in the serialized output
        fields = ['id', 'subject', 'details']