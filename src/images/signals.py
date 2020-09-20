from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


# Receives the signal from the implicit intermediate 'through' model of the many2many Image.users_like field.
@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes=instance.users_like.count()
    instance.save()