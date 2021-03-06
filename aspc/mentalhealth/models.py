from __future__ import unicode_literals

import django
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __unicode__(self):
        return self.name

class Insurance(Category):
    pass

class Qualification(Category):
    pass

class Specialty(Category):
    pass

class Tag(Category):
    pass

class Gender(Category):
    pass

class Identity(Category):
    pass

class SexualOrientation(Category):
    pass

class Ethnicity(Category):
    pass

class Therapist(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='profile', null=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=70, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    insurances = models.ManyToManyField(Insurance)
    specialties = models.ManyToManyField(Specialty)
    qualifications = models.ManyToManyField(Qualification)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class MentalHealthReview(models.Model):
    reviewer = models.ForeignKey(User)
    therapist = models.ForeignKey(Therapist, related_name='reviews')
    reasons = models.ManyToManyField(Specialty)
    duration = models.TextField()
    feeling = models.TextField()
    gender = models.ManyToManyField(Gender, blank=True)
    sexual_orientation = models.ManyToManyField(SexualOrientation, blank=True)
    ethnicity = models.ManyToManyField(Ethnicity, blank=True)
    identity = models.ManyToManyField(Identity, blank=True)
    identity_related_comment = models.TextField(null=True, blank=True)
    therapist_recommendation = models.TextField(null=True, blank=True)
    therapist_strategy = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_ts = models.DateTimeField(default=django.utils.timezone.now)

