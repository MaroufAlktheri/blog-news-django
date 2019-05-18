from django.urls import path
from .views import PostsListView, PostDetailView
urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='Post-detail'),
]