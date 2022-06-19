from django.contrib.auth.models import User
from django.urls import path

from .views import UserPostListView, PostCreateView, PostDetailView


urlpatterns = [
    path('post/<str:username>/', UserPostListView.as_view(), name='user-posts-list'),
    path('new-post/', PostCreateView.as_view(), name='post-form'),
    path('post-<slug:slug>-<int:pk>/detail/', PostDetailView.as_view(), name='user_detail_post'),

]
