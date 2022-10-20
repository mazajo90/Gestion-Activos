from django.urls import path

from .views import (UserListView,
                    UserCreateView,
                    UserUpdateView,
                    UserDetailView,
                    UserPageView,
                    UserSearchListView,
                    UserDeleteView)


users_patterns =([
    path('search', UserSearchListView.as_view(), name='search'),
    path('', UserListView.as_view(), name='users'),
    path('<int:pk>/<slug:slug>/', UserDetailView.as_view(), name='user'),
    path('<int:pk>/profile', UserPageView.as_view(), name='profile'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete'),
], 'users')