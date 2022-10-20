from django.views.generic import FormView, TemplateView
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.core.mail import EmailMultiAlternatives
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings
from django.db.models import Q

from .forms import AsignationForm
from .models import Asignation, AsignationHistory, AsignationState


def UserLog(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserLog, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name='dispatch')
class HomePageAsig(TemplateView): 
    template_name = "asignacion/asignation_list.html"


@method_decorator(staff_member_required, name='dispatch')    
class AsignationList(ListView):
    model = Asignation
    template_name = 'asignacion/asignation_list.html'
    queryset = Asignation.objects.all().order_by('pk')
    paginate_by = 10


@method_decorator(staff_member_required, name='dispatch')
class AsignationSearchListView(ListView):
    model = Asignation
    template_name = 'asignacion/asignation_list.html'
    
    def get_queryset(self):
        filters = (Q(asig_id__icontains=self.query()) 
                   | Q(product__product_name__icontains=self.query()) 
                   | Q(user__user_name__icontains=self.query())
                   | Q(user__user_last_name__icontains=self.query())
                   | Q(product__serial__icontains=self.query())
                   | Q(product__mac_address__icontains=self.query())
                   | Q(product__active_code__icontains=self.query()))
        return Asignation.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query()
        context["count"] = context['object_list'].count()
        return context


@method_decorator(staff_member_required, name='dispatch')
class AsignationDetailView(DetailView):
    model = Asignation
    template_name = 'asignacion/asignation_list.html'
    context_object_name = 'asignation'

@method_decorator(staff_member_required, name='dispatch')
class HistoryDetailView(DetailView):
    model = AsignationHistory
    template_name = "asignacion/history_profile.html"
    context_object_name = 'asignation'    


@method_decorator(staff_member_required, name='dispatch')           
class AsignationCreateView(SuccessMessageMixin, CreateView):
    model = Asignation
    form_class = AsignationForm
    success_url = reverse_lazy('asignation:list')
    success_message = 'Se ha asignado un producto exitosamente'
    
    def form_valid(self, form):
        form.send()
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class AsignationUpdateView(SuccessMessageMixin, UpdateView):
    model = Asignation
    form_class = AsignationForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('asignation:list')
    success_message = 'Asignacion editado correctamente'



@method_decorator(staff_member_required, name='dispatch')
class AsignationDelete(SuccessMessageMixin, DeleteView):
    model = Asignation
    success_url = reverse_lazy('asignation:list')
    success_message = 'Asignacion eliminada correctamente'


@method_decorator(staff_member_required, name='dispatch')    
class AsignationPageView(DetailView):
    model = Asignation
    template_name = "asignacion/check_list.html"
    queryset = Asignation.objects.all().order_by('pk')    
    context_object_name = 'asignation'
    paginate_by = 10


@method_decorator(staff_member_required, name='dispatch')
class AsignationHistoryListView(ListView):
    model = AsignationHistory
    template_name = 'asignacion/asignation_list.html'
    queryset = AsignationHistory.objects.all().order_by('pk')
    paginate_by = 10            
    
    
#Seccion de Historial-----Busqueda por filtros
@method_decorator(staff_member_required, name='dispatch')   
class HistorialListView(ListView):
    model = AsignationHistory
    template_name = 'asignacion/history_list.html'
    paginate_by = 10

class HistorialSearchListView(ListView):
    model = AsignationHistory
    template_name = 'asignacion/history_list.html'
    

    def get_queryset(self):
        filters = (Q(asig_id__icontains=self.query()) 
                   | Q(user__user_name__icontains=self.query())
                   | Q(user__user_last_name__icontains=self.query()) 
                   | Q(product__product_name__icontains=self.query()))
        return AsignationHistory.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query()
        context["count"] = context['object_list'].count()
        return context    
    

    