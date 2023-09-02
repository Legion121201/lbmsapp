# urls.py
from django.urls import path
from .views import UserList, UserDetail, BookList, BookDetail
from django.views.generic import TemplateView

urlpatterns = [
    path('api/users/', UserList.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('api/books/', BookList.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('', TemplateView.as_view(template_name='react_app.html')),
]
