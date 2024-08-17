from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    doj = models.DateField()
    address = models.TextField()
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class Student(Person):
    rno = models.IntegerField()

class Teacher(Person):
    subject = models.CharField(max_length=10,null=True,blank=True)
    salary = models.FloatField()

class Club(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    members = models.ManyToManyField('Student', related_name='clubs')
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    isbn = models.CharField(max_length=13, unique=True)
    available_copies = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Password length set by Django

    def __str__(self):
        return self.username