from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
	name = models.CharField(max_length=30)
	phone = models.CharField(max_length=11)
	email = models.CharField(max_length=50, blank=True, default='')
	address = models.CharField(max_length=150, blank=True, default='')

	def __str__(self):
		return self.name


class Vehicle(models.Model):
	type = models.CharField(max_length=30)
	title = models.CharField(max_length=50)
	capacity = models.CharField(max_length=30)

	def __str__(self):
		return self.title


class Post(models.Model):
	TYPE_CHOICES = (
		("WH", "warehouse"),
		("MO", "main office")
	)
	address = models.CharField(max_length=150)
	phone = models.CharField(max_length=9, blank=True, default='')
	type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='WH')
	total_space = models.CharField(max_length=30, blank=True, default='')

	def __str__(self):
		return self.address


class Worker(models.Model):
	first_name = models.CharField(max_length=30)
	mid_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	phone = models.CharField(max_length=9, blank=True, default='')
	email = models.CharField(max_length=50, blank=True, default='')
	address = models.CharField(max_length=150, blank=True, default='')
	position = models.CharField(max_length=50, blank=True, default='')
	pk_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return "{0} {1} {2}".format(self.first_name, self.last_name, self.mid_name)


class Trip(models.Model):
	TRIP_TYPE_CHOICES = (
		("C", "common"),
		("E", "express"),
	)
	trip_date = models.DateField
	trip_type = models.CharField(max_length=20, choices=TRIP_TYPE_CHOICES, default='C')
	pk_vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	pk_courier = models.ForeignKey(Worker, on_delete=models.CASCADE)


class Profile(models.Model):
	location = models.CharField(max_length=150, blank=True, default='')
	pk_user = models.OneToOneField(User, on_delete=models.CASCADE)


class Package(models.Model):
	TYPE_CHOICES = (
		("C", "common"),
		("E", "express"),
	)
	STATUS_CHOICES = (
		("S", "at thе sender"),
		("P", "at the post"),
		("R", "at the recipient"),
	)
	SIZE_CHOICES = (
		("S", "small box"),
		("M", "medium box"),
		("L", "large box"),
		("XL", "extra large box"),
		("WP", "wrapped parcel"),
		("DOC", "documents"),
	)
	ship_date = models.DateField(default=timezone.now)
	delivery_date = models.DateField(default=timezone.now)
	description = models.CharField(max_length=300, blank=True, default='')
	status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='S')
	type = models.CharField(max_length=30, choices=TYPE_CHOICES, default='C')
	size = models.CharField(max_length=5, choices=SIZE_CHOICES)
	from_address = models.CharField(max_length=150)
	from_phone = models.CharField(max_length=11)
	to_address = models.CharField(max_length=150)
	to_phone = models.CharField(max_length=11)
	pk_trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, blank=True)
	pk_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
	pk_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)




