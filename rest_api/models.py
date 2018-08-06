from django.db import models
from ip_collector.models import ProxyPool

# Create your models here.


class Token(models.Model):
    is_available = models.BooleanField(default=False, blank=True)
    token = models.CharField(max_length=256, blank=True, unique=True)
    latest_login = models.DateTimeField(blank=True)


class Request(models.Model):
    token = models.ForeignKey(Token, blank=True)
    request_time = models.DateTimeField(auto_now_add=True)
    proxy = models.ForeignKey(ProxyPool, blank=True)
