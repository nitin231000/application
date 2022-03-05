from django.urls import path,include
from poll.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('crud', views.PollViewSet, basename='poll')

urlpatterns = [
    path('',include(router.urls))
]
