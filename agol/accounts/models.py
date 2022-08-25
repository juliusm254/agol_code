from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.urls import reverse

from customers.models import Customer


class User(AbstractUser):
    class Types(models.TextChoices):
        OPERATIONS = "OPERATIONS", "OperationsUser"
        CUSTOMER = "CUSTOMER", "CustomerUser"

    base_type = Types.OPERATIONS

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=Types.OPERATIONS
    )
    customer_id = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.type
        return super().save(*args, **kwargs)


class OperationsManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return OperationsUser.objects.all()


class OperationsUser(User):
    base_type = User.Types.OPERATIONS
    # objects = OperationsManager()

    class Meta:
        proxy = True

    def whisper(self):
        return "whisper"
        

class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)


# class OperationsMore(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     gadgets = models.TextField()





# class CustomerMore(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    

class CustomerUser(User):
    base_type = User.Types.CUSTOMER
    objects = CustomerManager()

    @property
    def more(self):
        return self.customermore

    class Meta:
        proxy = True

    def accelerate(self):
        return "Go faster"