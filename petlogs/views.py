from .models import PetLog
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PetLogSerializer


class PetLogViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = PetLog.objects.all()
    # The serializer class for serializing output
    serializer_class = PetLogSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]