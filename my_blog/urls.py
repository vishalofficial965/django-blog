from django.urls import path,reverse,reverse_lazy
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(),name="blog-home"),
    path('post/<int:pk>/',views.post_details,name="post-detail"),
    path('user/<str:username>/',views.UserPostListView.as_view(),name="user-posts"),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name="post-delete"),
    path('post/new/',views.PostCreateView.as_view(),name="post-create"),
    path('about/',views.about,name="blog-about"),
]
