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

from .models import Phone
from .forms import PhoneForm


def UserLog(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserLog, self).dispatch(request, *args, **kwargs)
    


@method_decorator(staff_member_required, name='dispatch')
class PhoneListView(ListView):
    model = Phone
    template_name = 'phone_list.html'
    queryset = Phone.objects.all().order_by('pk')
    paginate_by = 10 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'Listado de Telefonos'
        return context   

@method_decorator(staff_member_required, name='dispatch')
class PhoneCreateView(SuccessMessageMixin, CreateView):
    model = Phone
    form_class = PhoneForm
    success_url = reverse_lazy('phones:phones')
    success_message = 'Producto creado exitosamente'

@method_decorator(staff_member_required, name='dispatch')
class PhoneUpdateView(SuccessMessageMixin, UpdateView):
    model = Phone
    form_class = PhoneForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('phones:phones')
    success_message = 'Producto editado correctamente'

@method_decorator(staff_member_required, name='dispatch')
class PhoneDeleteView(SuccessMessageMixin, DeleteView):
    model = Phone
    success_url = reverse_lazy('phones:phones')
    success_message = 'Producto eliminado correctamente'
        