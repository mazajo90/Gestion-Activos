from django.urls import path
from usuarios.api.views import UserListView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>', UserDetailView.as_view(), name='user_detail')
]