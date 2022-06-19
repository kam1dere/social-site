from django.contrib.auth.models import User
from django.urls import path

from .views import discussion_create, UserDiscussionsListView, DiscussionDetailView


urlpatterns = [
    path('discussions/<str:username>/', UserDiscussionsListView.as_view(), name='user_discussion'),
    # path('new-post/', DiscussionCreateView.as_view(), name='post-form'),
    path('discussion-<slug:slug>-<int:pk>/detail/', DiscussionDetailView.as_view(), name='user_detail_discussion'),
    path('create/', discussion_create, name='create'),

]
