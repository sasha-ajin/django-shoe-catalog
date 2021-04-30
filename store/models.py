from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Line(models.Model):
    brand = models.ManyToManyField(Brand)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Model(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    price = models.IntegerField()
    availability = models.BooleanField()

    def __str__(self):
        return self.name
