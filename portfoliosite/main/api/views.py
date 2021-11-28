from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.db.models import Q

from ..models import Portfolio, Image, Comment
from .serializers import PortfolioSerializer, ImageSerializer, CommentSerializer
from .permissions import IsPortfolioOwner, IsImageOwner, PermissionToCreateImage


class PortfolioAPIViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given portfolio.

    list:
    Return a list of all the existing portfolios.

    create:
    Create a new portfolio instance.

    update:
    Update the given portfolio

    delete:
    Delete the given portfolio
    """

    authentication_classes = (BasicAuthentication,)

    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    # Special permission to update
    def get_permissions(self):
        if self.action == 'update':
            permission_classes = (IsAuthenticated, IsPortfolioOwner)
        else:
            permission_classes = (IsAuthenticatedOrReadOnly,)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ImageAPIViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given image.

    list:
    Return a list of all the existing images.

    create:
    Create a new image instance.

    update:
    Update the given image

    delete:
    Delete the given image
    """

    authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Image.objects.all().order_by('-created')
    serializer_class = ImageSerializer

    def get_permissions(self):
        # if self.action == 'create':
        #     permission_classes = (IsAuthenticated, IsImageOwner)
        if self.action == 'update':
            permission_classes = (IsAuthenticated, IsImageOwner)
        else:
            permission_classes = (IsAuthenticatedOrReadOnly,)
        return [permission() for permission in permission_classes]


class CommentAPIViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given image.

    list:
    Return a list of all the existing images.

    create:
    Create a new image instance.
    """

    authentication_classes = (BasicAuthentication,)
    permission_classes = (AllowAny,)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class SearchAPIView(ListAPIView):
    """
    Return a query result by searching images by portfolio, name, description

    Required "q" param - query string
    """

    serializer_class = ImageSerializer

    def get_queryset(self):
        query_str = self.request.query_params['q']
        res = Image.objects.filter(Q(name__icontains=query_str) |
                                   Q(description__icontains=query_str) |
                                   Q(portfolio__name__icontains=query_str))  # add search by portfolios
        return res
