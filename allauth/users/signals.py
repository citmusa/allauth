# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    # print('saved: {}'.format(kwargs['instance'].__dict__))
    user = kwargs['instance']
    if kwargs['created']:
        profile = Profile(user=user)
        profile.save()
