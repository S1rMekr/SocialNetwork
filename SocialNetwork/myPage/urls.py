from django.urls import path
from . import views

app_name='myPage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('<int:pk>/add_post/', views.AddPost.as_view(), name='add_post'),
    path('<int:pk>/settings/', views.UserSettings.as_view(), name='settings'),
    path('delete/<int:pk>', views.deleteView,name='delete'),
    path('update/<int:pk>', views.updateView, name='update_post'),
    # path('<int:pk>/post/<int:post_pk>', views.PostDeleteView.as_view(), name='delete'),
    # # path('<int:pk>/<int:id>/', views.PostSettings.as_view(), name='post_settings'),
]