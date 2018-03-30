from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.signals import pre_save

from user.utils import unique_slug_generator


class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    address = models.CharField(max_length=95, null=True, blank=True)
    postcode = models.PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(999999)])
    street = models.CharField(max_length=80, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)

    email = models.EmailField(unique=True, max_length=50, null=False, blank=False)
    phone_number = models.CharField(unique=True, max_length=20, null=True, blank=True)

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.name

    def save(self,  *args, **kwargs):
        self.address = '{}, {}, {}'.format(str(self.postcode), self.street, self.state)
        super(User, self).save(*args, **kwargs)


# signal
def task_pre_save(sender, instance, *args, **kwargs):
    print('Saving..')
    instance.slug = unique_slug_generator(instance)


pre_save.connect(task_pre_save, sender=User)
