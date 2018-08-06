from django.db import models

# Create your models here.


class ProxyPool(models.Model):
    IP_TYPE_CHOICE = (
        ('http', 'http'),
        ('https', 'https'),
    )
    ip = models.IPAddressField(blank=True)
    port = models.IntegerField(blank=True)
    type = models.CharField(blank=True, max_length=20, choices=IP_TYPE_CHOICE)
    create_at = models.DateTimeField(auto_now_add=True)
    checked_at = models.DateTimeField(blank=True)