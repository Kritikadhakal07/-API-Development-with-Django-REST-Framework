from django.db import models

# Create your models here.
class Univeristy(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    program_name = models.CharField(max_length=100)
    univeristy=models.ForeignKey(Univeristy,on_delete=models.CASCADE,related_name='programs')

    def __str__(self):
        return self.program_name