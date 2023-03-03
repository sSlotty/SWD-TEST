from django.urls import path
from api import views

urlpatterns = [
    path('send/', views.SendEmailAPIView.as_view(), name='send_email'),
]