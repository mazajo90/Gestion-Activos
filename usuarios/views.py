from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.admin.filters import SimpleListFilter
from django.conf import settings

from .models import User
from .forms import UserForm

def UserLog(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserLog, self).dispatch(request, *args, **kwargs)
    
   

@method_decorator(staff_member_required, name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'usuarios/user_list.html'
    queryset = User.objects.all().order_by('pk')
    paginate_by = 1
    list_per_page = settings.LIST_PER_PAGE
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'Listado de Colaboradores' 
        return context
    

@method_decorator(staff_member_required, name='dispatch')
class UserDetailView(DetailView):
    model = User
    template_name = 'usuarios/user_list.html'
    context_object_name = 'user'

@method_decorator(staff_member_required, name='dispatch')   
class UserSearchListView(ListView):
    model = User
    template_name = 'usuarios/user_list.html'
    
    def get_queryset(self):
        filters = Q(user_name__icontains=self.query()) | Q(user_last_name__icontains=self.query()) |  Q(user_email__icontains=self.query()) | Q(user_name_corp__icontains=self.query()) |Q(id_user__icontains=self.query())
        return User.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query()
        context["count"] = context['object_list'].count()
        return context

@method_decorator(staff_member_required, name='dispatch')
class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:users')
    success_message = 'Se agregó colaborador exitosamente'
    
    

@method_decorator(staff_member_required, name='dispatch')
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('users:users')
    success_message = 'Colaborador editado correctamente'
    
        
@method_decorator(staff_member_required, name='dispatch')
class UserDeleteView( SuccessMessageMixin ,DeleteView):
    model = User
    success_url = reverse_lazy('users:users')
    success_message = 'Colaborador Eliminado del Sistema'

@method_decorator(staff_member_required, name='dispatch')
class UserPageView(DetailView):
    model = User
    template_name = "usuarios/user_profile.html"
    context_object_name = 'user'    
    
    
    
