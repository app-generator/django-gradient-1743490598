# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Visitor(models.Model):

    #__Visitor_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    passcode = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    phonenumber = models.TextField(max_length=255, null=True, blank=True)
    identificationno = models.TextField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    gender = models.TextField(max_length=255, null=True, blank=True)
    companyname = models.TextField(max_length=255, null=True, blank=True)
    purpose = models.TextField(max_length=255, null=True, blank=True)
    comment = models.TextField(max_length=255, null=True, blank=True)
    designationid = models.IntegerField(null=True, blank=True)
    employeeid = models.IntegerField(null=True, blank=True)
    checkindate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    checkoutdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    expecteddate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    expectedtime = models.DateTimeField(blank=True, null=True, default=timezone.now)
    qrcode = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)
    apppoved = models.BooleanField()
    approvaloutcome = models.TextField(max_length=255, null=True, blank=True)
    approvalcomment = models.TextField(max_length=255, null=True, blank=True)
    siteid = models.IntegerField(null=True, blank=True)

    #__Visitor_FIELDS__END

    class Meta:
        verbose_name        = _("Visitor")
        verbose_name_plural = _("Visitor")



#__MODELS__END
