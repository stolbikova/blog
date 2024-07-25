from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, AddCommentView, CommentApproveView, CommentRemoveView, DeletePostView
)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(),
         name='add_comment_to_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
    path('comment/<int:pk>/approve/',
         CommentApproveView.as_view(), name='comment_approve'),
    path('comment/<int:pk>/remove/',
         CommentRemoveView.as_view(), name='comment_remove'),
    # Auth
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]
