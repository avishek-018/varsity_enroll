from django.db import models

# Create your models here.
class student(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	b_date = models.DateTimeField('Birth Date')
	roll = models.CharField(max_length = 20)
	dept = models.CharField(max_length = 20)
	session  = models.CharField(max_length = 20)


class teacher(models.Model):
	name = models.CharField(max_length = 20)
	dept = models.CharField(max_length = 20)
	subject = models.CharField(max_length = 20)
	
