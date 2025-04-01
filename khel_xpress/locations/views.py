from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import State, District
from .serializers import StateSerializer, DistrictSerializer

class StateListView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class DistrictListView(generics.ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        state_id = self.kwargs['state_id']
        return District.objects.filter(state_id=state_id)
