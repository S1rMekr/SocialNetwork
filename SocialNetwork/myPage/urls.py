from django.urls import path
from . import views

app_name='myPage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.ProfileView.as_view(), name='profile')
]