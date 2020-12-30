from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Consulta(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tab_number = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=False)
    city = models.CharField(max_length = 5)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
   
    def calculate_age(self):
    	import datetime
    	return int ((datetime.datetime.now() - self.birthday).days / 365.25  )
    age = property(calculate_age)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name