from django.urls import path
from django.http import HttpResponseRedirect, request
from . import views

urlpatterns = [
    path('', views.home, name='poll-home'),
    path('create/', views.CreatePoll, name='create-poll'),
    path('<int:pk>/', views.DetailedPoll, name='detail-poll')
]