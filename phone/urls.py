from django.urls import path
from .views import (PhoneListView, 
                    PhoneCreateView, 
                    PhoneUpdateView, 
                    PhoneDeleteView) 
                    # ProductCreateView, 
                    # ProductPageView, 
                    # ProductSearchListView, 
                    # ProductWarehouseListView,
                    # ProductSearchListViewWarehouse)
#from . import views


phones_patterns =([
    path('', PhoneListView.as_view(), name='phones'),
    path('create/', PhoneCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PhoneUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PhoneDeleteView.as_view(), name='delete')
    #  path('search', ProductSearchListView.as_view(), name='search'),
    #  path('list_ware', ProductWarehouseListView.as_view(), name='list_ware'),
    #  path('<int:pk>/<slug:slug>/', ProductDetailView.as_view(), name='product'),
    #  path('<int:pk>/check_list', ProductPageView.as_view(), name='check_list'),
    #  path('search_notebook', ProductSearchListViewWarehouse.as_view(), name='search_notebook'),
], 'phones')
