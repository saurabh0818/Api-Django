from django.db import models


class student(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    standard = models.IntegerField()
    address = models.CharField(max_length=20)

    def __str__(self):
        return  self.fname




class payment(models.Model):

    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    payment = models.IntegerField()
    Date = models.DateTimeField()

    def __str__(self):
        return self.student_id.fname

# Create your models here.
