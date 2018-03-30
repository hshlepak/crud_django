import django_tables2 as tables
from .models import User


class UserTable(tables.Table):
    name = tables.TemplateColumn('<a href="/users/{{ record.slug }}/">{{ record.name }}</a>')

    class Meta:
        model = User
        exclude = ('id', 'postcode', 'street', 'state', 'slug', )
        template_name = 'django_tables2/table.html'

