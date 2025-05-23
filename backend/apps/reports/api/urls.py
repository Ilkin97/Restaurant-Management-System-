from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DailyReportViewSet


# DefaultRouter automatically generates the necessary URLs for the viewsets.
# It provides a simpler way to wire up the URLs for our views.
router = DefaultRouter()

# Register the DailyReportViewSet with the router.
# This creates the URL patterns that will be mapped to the actions (list, create, update, delete) of the DailyReportViewSet.
router.register(r'', DailyReportViewSet)

urlpatterns = [
    # Include all the URLs generated by the router and map them to the appropriate views.
    path('', include(router.urls)),
]
