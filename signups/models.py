from django.db import models

# Create your models here.
from django.utils.encoding import smart_unicode


class SignUp(models.Model):
    for_you = models.BooleanField(default=True, verbose_name="Is this purchase for you? If so, check this ")
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    email=models.EmailField(null=False, blank=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.email)
