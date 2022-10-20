from django.urls import path
from .views import (HomePageAsig, 
                   AsignationList, 
                   AsignationDetailView, 
                   AsignationCreateView, 
                   AsignationUpdateView, 
                   AsignationDelete, 
                   AsignationSearchListView, 
                   AsignationPageView,  
                   HistorialListView, 
                   AsignationHistoryListView,
                   HistorialSearchListView,
                   HistoryDetailView)
from . import views

asignation_patterns =([
     path('', AsignationList.as_view(), name='list'),
     path('search/', AsignationHistoryListView.as_view(), name='search'),
     path('search/asignation', AsignationSearchListView.as_view(), name='search/asignation'),
     path('search/historial', HistorialSearchListView.as_view(), name='search/historial'),
     path('history/', HistorialListView.as_view(), name='history'),
     path('<int:pk>/<slug:slug>/', AsignationDetailView.as_view(), name='detalle'),
     path('create/', AsignationCreateView.as_view(), name='create'),
     path('update/<int:pk>/', AsignationUpdateView.as_view(), name='update'),
     path('delete/<int:pk>/', AsignationDelete.as_view(), name='delete'),
     path('<int:pk>/check', AsignationPageView.as_view(), name='check'),
     path('<int:pk>/historial', HistoryDetailView.as_view(), name='historial'),
], 'asignation')   