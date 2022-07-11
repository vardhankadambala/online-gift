from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cart(models.Model):
	pname = models.CharField(max_length=10)
	pnum = models.CharField(max_length=10,blank=True,null=True)
	pcost =models.CharField(max_length=10,blank=True,null=True)
	
	def __str__(self):
		return self.pname


class cart1(models.Model):
	p_name = models.CharField(max_length=10)
	p_num = models.CharField(max_length=10,blank=True,null=True)
	p_cost =models.CharField(max_length=10,blank=True,null=True)
	p_cost2 =models.CharField(max_length=10,blank=True,null=True)
	u_name= models.CharField(max_length=20,blank=True,null=True)

	def __str__(self):
		return self.p_name