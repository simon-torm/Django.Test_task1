from rest_framework.permissions import BasePermission
from ..models import Portfolio


class IsPortfolioOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsImageOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.portfolio.author


# Permission to create an image for a specific portfolio
# Not finished!
class PermissionToCreateImage(BasePermission):
    def has_object_permission(self, request, view, obj):
        id_portfolio = request.data.get('portfolio')
        return request.user == Portfolio.objects.get(id=id_portfolio).author

