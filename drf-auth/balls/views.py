from rest_framework import generics
from .serializers import BallSerializer
from .models import Ball
from .permissions import IsOwnerOrReadOnly


class BallListCreate(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Ball.objects.all()
    serializer_class = BallSerializer


class BallDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Ball.objects.all()
    serializer_class = BallSerializer
