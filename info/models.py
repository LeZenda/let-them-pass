from django.db import models
from django_quill.fields import QuillField


class News(models.Model):
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    heading = models.CharField(max_length=200)
    news = QuillField(blank=True,null=True)

    def __str__(self):
        return f'News {self.id} - {self.heading}'

class Country(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    comments = QuillField(blank=True,null=True)

    def __str__(self):
        return f'Country {self.id} - {self.name}'



class Crossing(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    car_queue_length = models.IntegerField(blank=True,null=True)
    pedestrian_queue_length = models.IntegerField(blank=True,null=True)
    car_queue_wait_time = models.IntegerField(blank=True,null=True)
    comments = QuillField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()