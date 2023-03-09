from django.urls import path
from . import views



urlpatterns = [
    path("all_posts/", views.AllBlogView.as_view(), name="all_posts"),
    path("posts_detail/<int:pk>/", views.BlogDetailView.as_view(), name="posts_detail"),
    # Category
    path("all_categories/", views.CategoryListView.as_view(), name="all_categories"),
    path("category_detail/<int:pk>/", views.CategoryDetailView.as_view(), name="category_detail"),
]
