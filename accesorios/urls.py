from django.urls import path
from .views import (AccesoriosListView, 
                    AccesoriosDetailView, 
                    AccesoriosCreateView, 
                    AccesoriosUpdateView, 
                    AccesoriostDeleteView,
                    AccesoriosSearchListView,
                    AsignationDisplayListView,
                    AsignacionDisplayCreateView,
                    AsignationDisplaySearch,
                    HistorialDisplayListView,
                    HistorialDisplaySearch,
                    DisplaySearchWarehouseListView,
                    DisplayWarehouseListView)

accesorios_patterns =([
     path('', AccesoriosListView.as_view(), name='accesorios-list'),
     path('<int:pk>/<slug:slug>/', AccesoriosDetailView.as_view(), name='accesorio'),
     path('create/', AccesoriosCreateView.as_view(), name='create'),
     path('update/<int:pk>/', AccesoriosUpdateView.as_view(), name='update'),
     path('delete/<int:pk>/', AccesoriostDeleteView.as_view(), name='delete'),
     path('search', AccesoriosSearchListView.as_view(), name='search'),
     path('search_display', DisplaySearchWarehouseListView.as_view(), name='search_display'),
     path('asignacion-list', AsignationDisplayListView.as_view(), name='asignacion-list'),
     path('asignacion-create', AsignacionDisplayCreateView.as_view(), name='asignacion-create'),
     path('search/asignacion', AsignationDisplaySearch.as_view(), name='search/asignacion'),
     path('history/', HistorialDisplayListView.as_view(), name='history'),
     path('search/historial', HistorialDisplaySearch.as_view(), name='search/historial'),
     path('list_ware', DisplayWarehouseListView.as_view(), name='list_ware')
], 'accesorios')   