from django.urls import path, include
from .views import BookListView, BookDetailViews, BookCreateViews, BookDeleteViews, BookUpdateViews
urlpatterns = [
    path('list/', BookListView.as_view(), name='book-list'),
    path('detail/<int:pk>/', BookDetailViews.as_view(), name='book-detail'),
    path('create/', BookCreateViews.as_view(), name='book-create'),
    path('delete/<int:pk>/', BookDeleteViews.as_view(), name='book-delete'),
    path('update/<int:pk>/', BookUpdateViews.as_view(), name='book-update'),
]