from django.urls import path
from . import views

urlpatterns = [
    path('/', Home.home),
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('track/<int:request_id>/', views.track_service_request, name='track_service_request'),
]
