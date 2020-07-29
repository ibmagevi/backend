from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class User(AbstractUser):
    is_agent = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)

class Hospital(models.Model):
    name = models.CharField(max_length = 512)
    address = models.TextField()
    phone_number = models.CharField(max_length=13, unique=True)


AGENT_TYPE = [
    ('b', 'backend'),
    ('f', 'frontend')
]
gender_choices = (
    ('M', 'Male'),
    ('F', "Female"),
)
class AgentProfile(models.Model):
    user = models.OneToOneField('core.User', on_delete=models.CASCADE)
    hospital = models.ForeignKey('core.Hospital', on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, unique=True)
    gender = models.CharField(max_length = 1, choices = gender_choices)
    time_added = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=AGENT_TYPE, null=True)
    available = models.BooleanField(default=True)

class UserProfile(models.Model):
    user = models.OneToOneField('core.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, unique=True)
    gender = models.CharField(max_length = 1, choices = gender_choices)
    time_added = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

class Report(models.Model):
    user = models.ForeignKey('core.User', on_delete = models.CASCADE)
    positive = models.BooleanField()
    hospital = models.ForeignKey('core.Hospital', on_delete = models.CASCADE)
    fees = models.PositiveSmallIntegerField()

class HospitalComments(models.Model):
    user = models.ForeignKey('core.UserProfile', on_delete = models.CASCADE)
    hospital = models.ForeignKey('core.Hospital', on_delete = models.CASCADE)
    comment = models.TextField()

class TestingSlotBooking(models.Model):
    user = models.ForeignKey('core.UserProfile', on_delete = models.CASCADE)
    hospital = models.ForeignKey('core.Hospital', on_delete=models.CASCADE)
    test_datetime = models.DateTimeField()
    add_datetime = models.DateTimeField(auto_now_add = True)

class QuarantineBed(models.Model):
    hospital = models.ForeignKey('core.Hospital', on_delete=models.CASCADE)
    bed_number = models.PositiveSmallIntegerField()
    charges = models.PositiveSmallIntegerField()

class QuarantineBedBooking(models.Model):
    user = models.ForeignKey('core.UserProfile', on_delete = models.CASCADE)
    bed = models.ForeignKey('core.QuarantineBed', on_delete=models.CASCADE)
    booking_datetime = models.DateTimeField(auto_now_add = True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(blank = True, null=True)




