from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    level = models.IntegerField()
    student_int = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Plan(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    Status = (['done', 'done'],
              ['not done', 'not done'],
              )
    status = models.CharField(max_length=50, choices=Status)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
