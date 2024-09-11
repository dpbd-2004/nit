from django.db import models

# Create your models here.
class student(models.Model):
  name = models.CharField(max_length=100)
  dept = models.CharField(max_length=100)

  def __str__(self) -> str:
    return f"name: {self.name}, dept: {self.dept}"
  