from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import OrderItem, Product
from django.db.models import F

@receiver(post_save, sender=OrderItem)
def update_product_stock(sender, instance, **kwargs):
    product = instance.product
    product.stock = F('stock') - instance.quantity 
    product.save()