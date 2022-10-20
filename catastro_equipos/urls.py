from django.urls import path
from .views import (ProductListView, 
                    ProductDetailView, 
                    ProductCreateView, 
                    ProductUpdateView, 
                    ProductDeleteView, 
                    ProductPageView, 
                    ProductSearchListView, 
                    ProductWarehouseListView,
                    ProductSearchListViewWarehouse)
#from . import views


products_patterns =([
     path('search', ProductSearchListView.as_view(), name='search'),
     path('', ProductListView.as_view(), name='products'),
     path('list_ware', ProductWarehouseListView.as_view(), name='list_ware'),
     path('<int:pk>/<slug:slug>/', ProductDetailView.as_view(), name='product'),
     path('<int:pk>/check_list', ProductPageView.as_view(), name='check_list'),
     path('create/', ProductCreateView.as_view(), name='create'),
     path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
     path('search_notebook', ProductSearchListViewWarehouse.as_view(), name='search_notebook'),
     path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete')
], 'products')

  