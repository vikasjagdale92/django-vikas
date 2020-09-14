# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200, default="")
    option_A	  = models.CharField(max_length=200, default='')
    option_B	  = models.CharField(max_length=200, default='')
    option_C	  = models.CharField(max_length=200, default='')
    option_D	  = models.CharField(max_length=200, default='')
    answer		  = models.CharField(max_length=200, default='')
    pub_date      = models.DateTimeField('date published')
    def __str__(self):
  		return self.question_text

class StudentMaster(models.Model):
	first_name    = models.CharField(max_length=200, default='')
	last_name     = models.CharField(max_length=200, default='')
	DOB           = models.DateField('date of birth')
	gender        = models.CharField(max_length=200, default="")
	blood_group   = models.CharField(max_length=200, default='')
	standard      = models.CharField(max_length=200, default='')
	mobile_number = models.CharField(max_length=200, default='')
	school_name   = models.CharField(max_length=200, default='')
	address       = models.CharField(max_length=200, default='')
	country       = models.CharField(max_length=200, default='')
	state         = models.CharField(max_length=200, default="")
	city          = models.CharField(max_length=200, default="")
	pincode       = models.CharField(max_length=200, default='')
	# question      = models.ForeignKey(Question, on_delete=models.CASCADE)
	def __str__(self):
		return self.first_name+' '+self.last_name