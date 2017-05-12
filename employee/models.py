from __future__ import unicode_literals

from django.db import models

# Create your models here.
class employee_data(models.Model):
	name=models.CharField(max_length=100,null=True,blank=True)
	email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
	manager=models.ForeignKey("employee_data",null=True,blank=True)
	def __unicode__(self):
		return self.name

# class hierarchy_data(models.Model):
# 	junior=models.ForeignKey(employee_data,null=True)
# 	senior=models.ForeignKey(employee_data,null=True)