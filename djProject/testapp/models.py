from django.db import models

# Create your models here.
class deljobs (models.Model):
	date=models.DateField();
	company=models.CharField(max_length=100);
	title= models.CharField(max_length=100);
	eligibility= models.CharField(max_length=100);
	address= models.CharField(max_length=100);
	email=models.EmailField();
	phonenumber=models.IntegerField()
	def __unicode__(self):
		return self.description

class hyjobs (models.Model):
	date=models.DateField();
	company=models.CharField(max_length=100);
	title= models.CharField(max_length=100);
	eligibility= models.CharField(max_length=100);
	address= models.CharField(max_length=100);
	email=models.EmailField();
	phonenumber=models.IntegerField()
	def __unicode__(self):
		return self.description
class mumjobs (models.Model):
	date=models.DateField();
	company=models.CharField(max_length=100);
	title= models.CharField(max_length=100);
	eligibility= models.CharField(max_length=100);
	address= models.CharField(max_length=100);
	email=models.EmailField();
	phonenumber=models.IntegerField()
	def __unicode__(self):
		return self.description

