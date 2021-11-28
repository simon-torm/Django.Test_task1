from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('portfolios',
                views.PortfolioAPIViewSet,
                basename='portfolio')
router.register('images',
                views.ImageAPIViewSet,
                basename='image')
router.register('comments',
                views.CommentAPIViewSet,
                basename='comment')
urlpatterns = router.urls
urlpatterns += [path('search/', views.SearchAPIView.as_view(), name='SearchAPIView')]

