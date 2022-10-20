from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, EmailMessage, send_mail
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.template.loader import get_template
from asignacion.models import *


from .models import Product
from asignacion.models import Asignation
from .forms import ProductForm


def UserLog(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserLog, self).dispatch(request, *args, **kwargs)
    
        
@method_decorator(staff_member_required, name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'catastro_equipos/product_list.html'
    queryset = Product.objects.all().order_by('pk')
    paginate_by = 10
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'Listado de Productos' 
        return context

@method_decorator(staff_member_required, name='dispatch')
class ProductWarehouseListView(ListView):
    model = Product
    template_name = 'catastro_equipos/warehouse_list.html'
    queryset = Product.objects.all().order_by('pk')
    paginate_by = 10

    def get_queryset(self):
        exclude_pk = list(Asignation.objects.filter().order_by('product_id').distinct().values_list('product_id', flat=True))
        return Product.objects.filter().exclude(id_product__in=exclude_pk)

   
@method_decorator(staff_member_required, name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catastro_equipos/product_list.html'
    context_object_name = 'product'

    
@method_decorator(staff_member_required, name='dispatch')   
class ProductSearchListView(ListView):
    model = Product
    template_name = 'catastro_equipos/product_list.html'
    
    def get_queryset(self):
        filters = (Q(product_name__icontains=self.query())
                   | Q(mac_address__icontains=self.query()) 
                   | Q(active_code__icontains=self.query()) 
                   | Q(serial__icontains=self.query()))
        return Product.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query()
        context["count"] = context['object_list'].count()
        return context

@method_decorator(staff_member_required, name='dispatch')
class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:products')
    success_message = 'Producto creado exitosamente'
    
    
    #Para llamar otro forms agregar en la vista "secund_form_class = Nombre del Formulario"
    # def get_context_data(self, **kwargs):
    #     context = super(ProductCreateView, self).get_context_data(**kwargs)
    #     context['form'] = self.form_class(self.request.GET)
    #     if 'form_2' not in context:
    #         context['form_2'] = self.secund_form_class(self.request.GET)
    #     return context    
    
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object
    #     form = self.form_class(request.POST)
    #     form_2 = self.secund_form_class(request.POST)
    #     if form.is_valid() and form_2.is_valid():
    #         product_create = form.save( commit = False )
    #         product_status = form_2.save()
    #         product_create.save()
    #         return HttpResponseRedirect(self.get_success_url())
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form, form_2=form_2))

@method_decorator(staff_member_required, name='dispatch')
class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('products:products')
    success_message = 'Producto editado correctamente' 


@method_decorator(staff_member_required, name='dispatch')
class ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:products')
    success_message = 'Producto eliminado correctamente'


@method_decorator(staff_member_required, name='dispatch')
class HomePageView(TemplateView):

    template_name = "layout/home.html"

@method_decorator(staff_member_required, name='dispatch')
class ProductPageView(DetailView):
    model = Product
    template_name = "catastro_equipos/check_list.html"    
    context_object_name = 'product'

#Busqueda de productos en Bodega o "Notebook's Disponibles"    
@method_decorator(staff_member_required, name='dispatch')   
class ProductSearchListViewWarehouse(ListView):
    model = Product
    template_name = 'catastro_equipos/warehouse_list.html'
    
    def get_queryset(self):
        filters = (Q(product_name__icontains=self.query())
                   | Q(mac_address__icontains=self.query()) 
                   | Q(active_code__icontains=self.query()) 
                   | Q(serial__icontains=self.query()))
        exclude_pk = list(Asignation.objects.filter().order_by('product_id').distinct().values_list('product_id', flat=True))
        return Product.objects.filter(filters).exclude(id_product__in=exclude_pk)
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query()
        context["count"] = context['object_list'].count()
        return context

    
    