from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, AddCommentView, CommentApproveView, CommentRemoveView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', CommentApproveView.as_view(), name='comment_approve'),
    path('comment/<int:pk>/remove/', CommentRemoveView.as_view(), name='comment_remove'),
]
