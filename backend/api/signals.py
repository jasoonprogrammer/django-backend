from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import *
# from yourapp.models import Administrator

@receiver(post_save , sender = User)
def setUserPassword(sender , instance , created , **kwargs):
    # instance is the object of the User model which has just been created and it fired this signal .
    print(instance.password)
    if created:
        instance.set_password(instance.password)
        instance.save()


@receiver(post_save , sender = Sale)
def setQuantity(sender , instance , created , **kwargs):
    # instance is the object of the User model which has just been created and it fired this signal .
    if created:
        product = instance.product
        product.quantity = instance.quantity
        product.save()
