import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import User


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter()

    class Meta:
        model = User
        fields = '__all__'


class UserFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        'name',
        Submit('submit', 'Apply Filter'),
    )
