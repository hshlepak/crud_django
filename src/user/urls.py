from django.conf.urls import url
from .views import UserListView, UserCreateView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
    url(r'^users/$', UserListView.as_view(), name='users'),
    url(r'^users/create/$', UserCreateView.as_view(), name='add_user'),
    url(r'^users/(?P<slug>[\w-]+)/$', UserDetailView.as_view(), name='user'),
    url(r'^users/(?P<slug>[\w-]+)/edit/$', UserUpdateView.as_view(), name='edit_user'),
    url(r'^users/(?P<slug>[\w-]+)/delete/$', UserDeleteView.as_view(), name='delete_user'),
    url(r'^', UserListView.as_view(), name='home'),
]
