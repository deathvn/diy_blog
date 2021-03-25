from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post-lists/', views.BlogListView.as_view(), name='blogs'),
    path('post/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('authors/', views.BlogAuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.BlogListbyAuthorView.as_view(), name='blog-author'),
    path('post/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog-comment'),
    path('comment/<int:pk>/delete/', views.BlogCommentDelete.as_view(), name='blog-comment-delete'),
    path('comment/<int:pk>/update/', views.BlogCommentUpdate.as_view(), name='blog-comment-update'),
]