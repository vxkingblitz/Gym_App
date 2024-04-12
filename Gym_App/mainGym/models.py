from django.db import models


class Exersises(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    weight = models.IntegerField(blank = False)
    repeats = models.IntegerField(blank = False)
    approaches = models.IntegerField(blank = False)

    def __str__(self):
        return f'{self.name}'
    
class Calendar(models.Model):
    day = models.DateField()
    work_day_name = models.CharField(max_length = 50, blank = False)

    def __str__(self):
        return f'{self.day}, {self.work_day_name}'

#Гадигадагуду


