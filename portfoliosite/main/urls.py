from django.urls import path
from . import views


urlpatterns = [
    # portfolio views
    path('', views.feed, name='feed'),
    path("portfolio/<int:id>",
         views.portfolio_detail,
         name='portfolio_detail')
]