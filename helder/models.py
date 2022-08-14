from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3= models.ImageField(null=True, blank=True)
    image4= models.ImageField(null=True, blank=True)
    imgname=models.CharField(max_length=500)
    date=models.CharField(max_length=100)
    size=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    detail1=models.CharField(max_length=500)
    detail2=models.CharField(max_length=500)
    detail3=models.CharField(max_length=500)
    detail4=models.CharField(max_length=500)
    detail5=models.CharField(max_length=500)
    def __str__(self):
        return self.description
