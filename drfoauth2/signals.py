# from http://www.yeti.co/blog/oauth2-with-django-rest-framework/

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from oauth2_provider.models import Application

import datetime

#@receiver(post_save, sender=User)
def create_auth_client(sender, instance=None, created=False, **kwargs):
    """
    Intended to be used as a receiver function for a `post_save` signal
    on a custom User model
    Creates client_id and client_secret for authenticated users
    """
    if created:
        now = datetime.datetime.now()
        app = Application.objects.create(user=instance,
                                   client_type=Application.CLIENT_CONFIDENTIAL,
                                   authorization_grant_type=Application.GRANT_IMPLICIT,
                                   name=now.strftime("%Y-%m-%d %H:%M"),
                                   redirect_uris="oauthdrf://oauth.ios/callback")
        print("signals.create_auth_client: %s" % app)
        instance.set_password(instance.password)
        instance.save()

post_save.connect(create_auth_client, sender=User)

class Noop(models.Model):
    pass
