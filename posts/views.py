from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Advisor
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Advisor.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
