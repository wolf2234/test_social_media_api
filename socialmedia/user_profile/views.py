from django.shortcuts import render
from .models import UserProfile
from .serializers import ProfileSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



