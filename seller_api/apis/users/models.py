from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
import pytz

""" Seller user model
    It always mark as best practice to create custom user model as 
    requirement could be flexible with time, the reason it is ease for 
    the developer to mould the requirement in the execution 
"""


class Seller(AbstractUser):
    email = models.EmailField(null=False)
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class SellerGroup(Group):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, parent_link=True)
    status = models.BooleanField(default=1)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)