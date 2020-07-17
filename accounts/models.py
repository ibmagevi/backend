from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """
    User manager
    """
    def _create_user(self, username, email, password, is_staff, is_superuser, is_admin,
                     is_agent, is_contact, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not email:
            raise ValueError('Users must either be an agent or a contact')

        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            is_admin=is_admin,
            is_agent=is_agent,
            is_contact=is_contact,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, is_agent, is_contact, **extra_fields):
        return self._create_user(username, email, password, False, False, False, is_agent, is_contact, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True, True, False, True ** extra_fields)
        return user


# custom user
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=25, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    email_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    # The contacts (It's a contact tracing app)
    is_contact = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()


# TODO: Add differnt formats
# currently only works with Kenyan numbers
def validate_phone(value):
    if len(value) != 13:
        raise ValidationError(
            _('%(value)s is not a correct phone number.'),
            params={'value': value},
        )
    if value[0] != "+" or value[1] != "2" or value[2] != "5" or value[3] != "4":
        raise ValidationError(
            _('%(value)s is not a correct Kenyan phone number.'),
            params={'value': value},
        )


class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=13,
                                    unique=True, validators=[validate_phone])
    GENDER_CHOICES = [
        ('m', 'male'),
        ('f', 'female')]
    gender = models.CharField(
        max_length=50, choices=GENDER_CHOICES, null=True)
    is_active = models.BooleanField(default=True)
    #
    time_added = models.DateTimeField(
        auto_now_add=True)
    time_last_edited = models.DateTimeField(
        auto_now_add=True)
    #
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, editable=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']
