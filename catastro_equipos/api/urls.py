from django.urls import path
#from catastro_equipos.api.views import product_list, product_detail
from catastro_equipos.api.views import ProductListView, ProductDetailView


urlpatterns =[
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail')
]