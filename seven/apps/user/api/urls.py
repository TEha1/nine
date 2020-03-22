from django.urls import path, include
# from .views import UserCL, UserRUD, FollowCL, FollowRUD, UploadCL, UploadRUD
from rest_framework import routers

from .views import UserRegisterView, UserLoginView, UserRUD, UserListView, ChangePasswordView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('users/', UserListView.as_view()),
    path('user/<int:pk>/', UserRUD.as_view()),
    path('user/<int:pk>/changepassword/', ChangePasswordView.as_view()),

]
