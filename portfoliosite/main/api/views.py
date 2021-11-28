from rest_framework import generics
from rest_framework import viewsets
from ..models import Portfolio, Image, Comment
from .serializers import PortfolioSerializer, ImageSerializer, CommentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny


class PortfolioAPIViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ImageAPIViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Image.objects.all().order_by('-created')
    serializer_class = ImageSerializer


class CommentAPIViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
`