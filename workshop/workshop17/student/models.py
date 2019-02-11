from django.db import models

# Create your models here.
class Student(models.Model): # 이미 구현된 모델을 상속받음.
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
        return str(self.age)