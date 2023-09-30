from django.urls import path
from . import views

app_name='myPage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('<int:pk>/add_post/', views.AddPost.as_view(), name='add_post'),
    path('<int:pk>/settings/', views.UserSettings.as_view(), name='settings')
]