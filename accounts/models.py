from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.urls import reverse

from customers.models import Customer

# class CustomAccountManager(BaseUserManager):

#     def create_superuser(self, email, user_name, first_name, password, **other_fields):

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')

#         return self.create_user(email, user_name, first_name, password, **other_fields)

#     def create_user(self, customer, email, user_name, first_name, password, **other_fields):

#         if not email:
#             raise ValueError(_('You must provide an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, customer=customer, user_name=user_name,
#                           first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_staff(self, email, user_name, first_name, password, **other_fields):

#         if not email:
#             raise ValueError(_('You must provide an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name,
#                           first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user


# class CustomUser(AbstractBaseUser, PermissionsMixin):

#     email = models.EmailField(_('email address'), unique=True)
#     customer = models.ForeignKey(
#         Customer, on_delete=models.SET_NULL, null=True) 
#     user_name = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     start_date = models.DateTimeField(default=timezone.now)
#     about = models.TextField(_(
#         'about'), max_length=500, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     objects = CustomAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_name', 'first_name']

#     def __str__(self):
#         return self.user_name


class User(AbstractUser):
    class Types(models.TextChoices):
        OPERATIONS = "OPERATIONS", "OperationsUser"
        CUSTOMER = "CUSTOMER", "CustomerUser"

    base_type = Types.OPERATIONS

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
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
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.OPERATIONS)


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.CUSTOMER)


# class OperationsMore(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     gadgets = models.TextField()


class OperationsUser(User):
    base_type = User.Types.OPERATIONS
    objects = OperationsManager()

    class Meta:
        proxy = True

    def whisper(self):
        return "whisper"


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