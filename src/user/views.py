from django.db.models import Q, CharField
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_tables2 import RequestConfig

from .filters import UserFilter, UserFilterFormHelper
from .tables import UserTable
from .forms import UserForm
from .models import User


class UserListView(ListView):
    model = User
    filter_class = UserFilter
    formhelper_class = UserFilterFormHelper
    template_name = 'users.html'

    def get_queryset(self):
        return User.objects.all()
        # search = self.request.GET.get('search')
        # order = self.request.GET.get('order_by')
        # if search:
        #     fields = [f for f in User._meta.fields if isinstance(f, CharField)]
        #     queries = [Q(**{f.name: search}) for f in fields]
        #     qs = Q()
        #     for query in queries:
        #         qs = qs | query
        #     return User.objects.filter(qs)
        # elif order:
        #     return User.objects.all().order_by(order)
        # else:
        #     return User.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        filter = UserFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = UserFilterFormHelper()
        table = UserTable(filter.qs)
        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context


class UserDetailView(DetailView):
    queryset = User.objects.all()
    template_name = 'user_detail.html'

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(User, slug=slug)
        return obj


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'add_user.html'
    success_url = "/users/"

    def form_valid(self, form):
        form.save(commit=False)
        return super(UserCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(UserCreateView, self).get_context_data(*args, **kwargs)
        return context


class UserUpdateView(UpdateView):
    form_class = UserForm
    template_name = 'edit_user.html'
    success_url = "/users/"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(User, slug=slug)
        return obj


class UserDeleteView(DeleteView):
    form_class = UserForm
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('users')

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(User, slug=slug)
        return obj
