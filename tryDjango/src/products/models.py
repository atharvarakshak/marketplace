from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description =models.TextField(blank=True,null=True)
    price = models.TextField()
    summary =models.TextField(blank=False,null=False)
    feature = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})
