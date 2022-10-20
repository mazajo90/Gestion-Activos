from django.shortcuts import render
from django.contrib.auth import forms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.db.models import Q

from .models import DisplayPC, AsignationDisplay, AsignationDisplayHistory
from .forms import DisplayPCForm, AsignationDisplayForm

def UserLog(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserLog, self).dispatch(request, *args, **kwargs)


@method_decorator(staff_member_required, name='dispatch')
class AccesoriosListView(ListView):
    model = DisplayPC
    template_name = 'accesorios/accesorio_list.html'
    queryset = DisplayPC.objects.all().order_by('pk')
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'Listado de Productos' 
        return context
    
@method_decorator(staff_member_required, name='dispatch')
class AccesoriosDetailView(DetailView):
    model = DisplayPC
    template_name = 'accesorios/accesorio_list.html'
    context_object_name = 'accesorios'
    

@method_decorator(staff_member_required, name='dispatch')
class AccesoriosCreateView(SuccessMessageMixin, CreateView):
    model = DisplayPC
    form_class = DisplayPCForm
    success_url = reverse_lazy('accesorios:accesorios-list')
    success_message = 'Producto creado exitosamente'    


@method_decorator(staff_member_required, name='dispatch')
class AccesoriosUpdateView(SuccessMessageMixin, UpdateView):
    model = DisplayPC
    form_class = DisplayPCForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('accesorios:accesorios-list')
    success_message = 'Producto editado correctamente'     
    

@method_decorator(staff_member_required, name='dispatch')
class AccesoriostDeleteView(SuccessMessageMixin, DeleteView):
    model = DisplayPC
    success_url = reverse_lazy('accesorios:accesorios-list')
    success_message = 'Producto eliminado correctamente'    

#Vista para la busqueda
@method_decorator(staff_member_required, name='dispatch')   
class AccesoriosSearchListView(ListView):
    model = DisplayPC
    template_name = 'accesorios/accesorio_list.html'
    
    def get_queryset(self):
        filters = (Q(display_name__icontains=self.query()) 
         | Q(display_model__icontains=self.query())
         | Q(display_size__icontains=self.query())
         | Q(product_status__product_status__icontains=self.query()))
        return DisplayPC.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query()
        context["count"] = context['object_list'].count()
        return context


#Vista Asignacion de Pantalla
@method_decorator(staff_member_required, name='dispatch')
class AsignationDisplayListView(ListView):
    model = AsignationDisplay
    template_name = 'accesorios/asignacion_list.html'
    queryset = AsignationDisplay.objects.all().order_by('pk')
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'Listado de Asiganciones' 
        return context

@method_decorator(staff_member_required, name='dispatch')
class AsignacionDisplayCreateView(SuccessMessageMixin, CreateView):
    model = AsignationDisplay
    form_class = AsignationDisplayForm
    success_url = reverse_lazy('accesorios:asignacion-list')
    success_message = 'Asignación creado exitosamente'        


#Vista para busqueda de Asignacion de Pantalla
@method_decorator(staff_member_required, name='dispatch')
class AsignationDisplaySearch(ListView):
    model = AsignationDisplay
    template_name = 'accesorios/asignacion_list.html'
    
    def get_queryset(self):
        filters = (Q(user__user_name__icontains=self.query())
                   | Q(display_name__display_name__icontains=self.query())
                   | Q(display_name__asig_id__icontains=self.query()))
        return AsignationDisplay.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query()
        context["count"] = context['object_list'].count()
        return context    
    
#Vista para el historial de pantallas
@method_decorator(staff_member_required, name='dispatch')   
class HistorialDisplayListView(ListView):
    model = AsignationDisplayHistory
    template_name = 'accesorios/history_display_list.html'
    
    
class HistorialDisplaySearch(ListView):
    model = AsignationDisplayHistory
    template_name = 'accesorios/history_display_list.html'

    def get_queryset(self):
        filters = (Q(asig_id__icontains=self.query()) 
                   | Q(user__user_name__icontains=self.query()) 
                   | Q(display_name__asig_id__icontains=self.query())
                   | Q(display_name__display_name__icontains=self.query()))
        return AsignationDisplayHistory.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query()
        context["count"] = context['object_list'].count()
        return context    


#Vista para pantallas por asignar
@method_decorator(staff_member_required, name='dispatch')
class DisplayWarehouseListView(ListView):
    model = DisplayPC
    template_name = 'accesorios/warehouse_list.html'
    queryset = DisplayPC.objects.all().order_by('pk')
    paginate_by = 10

    def get_queryset(self):
        exclude_pk = list(AsignationDisplay.objects.filter().order_by('display_name_id').distinct().values_list('display_name_id', flat=True))
        return DisplayPC.objects.filter().exclude(id_product__in=exclude_pk)
    
#Vista para busqueda de pastallas por asignar 
@method_decorator(staff_member_required, name='dispatch')    
class DisplaySearchWarehouseListView(ListView):
    model = DisplayPC
    template_name = 'accesorios/warehouse_list.html'
    queryset = DisplayPC.objects.all().order_by('pk')
    paginate_by = 10

    def get_queryset(self):
        filters = (Q(display_name__icontains=self.query()) 
         | Q(display_model__icontains=self.query())
         | Q(display_size__icontains=self.query())
         | Q(product_status__product_status__icontains=self.query()))
        exclude_pk = list(AsignationDisplay.objects.filter().order_by('display_name_id').distinct().values_list('display_name_id', flat=True))
        return DisplayPC.objects.filter(filters).exclude(id_product__in=exclude_pk)
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query()
        context["count"] = context['object_list'].count()
        return context    
       
    