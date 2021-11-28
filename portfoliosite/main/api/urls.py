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


# urlpatterns = [
#     path('api/portfolios/',
#          views.PortfolioListView.as_view(),
#          name='portfolio_list'),
#     path('api/portfolio/<int:pk>',
#          views.PortfolioDetailView.as_view(),
#          name='portfolio_detail'),
#     path('api/portfolio/create',
#          views.PortfolioCreateView.as_view(),
#          name='portfolio_detail')
# ]
