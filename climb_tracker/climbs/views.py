from climbs.models import Area, Location, Route, Session
from rest_framework import viewsets
from .serializers import (LocationSerializer, AreaSerializer, RouteSerializer,
                          SessionSerializer)

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AreaViewSet(viewsets.ModelViewSet):
        queryset = Area.objects.all()
        serializer_class = AreaSerializer

class RouteViewSet(viewsets.ModelViewSet):
        queryset = Route.objects.all()
        serializer_class = RouteSerializer

class SessionViewSet(viewsets.ModelViewSet):
        queryset = Session.objects.all()
        serializer_class = SessionSerializer
