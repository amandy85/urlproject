from django.db import models

# Create your models here.
from shortner.models import UrlprojectURL

class ClickEventManager(models.Manager):
    def create_event(self, urlprojectInstance):
        if isinstance(urlprojectInstance, UrlprojectURL):
            obj,created = self.get_or_create(urlproject_url=urlprojectInstance)
            obj.count +=1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    # urlproject_url  = models.OneToOneField(UrlprojectURL)
    urlproject_url  = models.OneToOneField(UrlprojectURL, on_delete=models.CASCADE)
    count           = models.IntegerField(default=0)
    updated         = models.DateField(auto_now=True) 
    timestamp       = models.DateField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)