from django.db import models
#from django.db.models import Q

class Person(models.Model):
    name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
#Person.objects.filter(age__range=(10, 20))



#CREATE TABLE Person(id int,name varchar(50),age int NOT NULL,
#gender varchar(10));

#person = Person.objects.get(id=1)
#person.age = 25
#person.save()

