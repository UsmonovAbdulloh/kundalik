from django.db import models
from datetime import datetime
# Create your models here.
class PersonModel(models.Models):
    name = models.CharField(max_length=65,default='')
    fname = models.CharField(max_length=65,default='')
    date_of_birth = models.DateField(default=datetime.now())
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class StudentModel(PersonModel):
    active = models.BooleanField(default=True)
    username = models.CharField(max_length=65,default='')
    password = models.CharField(max_length=65,default='')
    phone = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'