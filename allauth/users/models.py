# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


USER_TYPES = {
    ('ADMIN', 'admin'),
    ('WORKER1', 'Worker1'),
    ('WORKER2', 'Worker2'),
    ('APPROVER1', 'Approver1'),
    ('APPROVER2', 'Approver2'),
    ('SUPERVISOR', 'Supervisor'),
}


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class WorkerProfile(models.Model):
    """ Abstract models to know with type of user has some fields """
    worker_id = models.CharField(max_length=20, blank=True)

    class Meta:
        abstract = True


class ApproverProfile(models.Model):
    """ Abstract models to know with type of user has some fields """
    approver_field = models.CharField(max_length=20, blank=True)

    class Meta:
        abstract = True


class Profile(WorkerProfile, ApproverProfile):
    user = models.OneToOneField(User)
    about = models.TextField()
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='WORKER1')

    def __str__(self):
        return "%s" % self.user.get_full_name()
