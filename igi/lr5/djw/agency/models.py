from django.db import models

from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

import logging 

logging.basicConfig(
    level=logging.INFO, filename='logs.log', filemode='a', format='%(asctime)s %(levelname)s %(message)s')

class UserRoleTypes:
    CLIENT = "client"
    STAFF = "staff"

class HotelRatings:
    TERRIBLE = 1
    BAD = 2
    MEDIUM = 3
    GOOD = 4
    EXCELLENT = 5

class TripAvalableDurations:
    ONE_WEEK = 7
    TWO_WEEKS = 14
    FOUR_WEEKS = 28

class DataStoringConfiguration:
    UPLOAD_IMAGES_TO = 'images/'

class User(AbstractUser):
    ROLE_TYPE_CHOICES = {
        UserRoleTypes.CLIENT: "client",
        UserRoleTypes.STAFF: "staff"
    }

    timezone = models.CharField(max_length=32, default='UTC')
    role = models.CharField(max_length=6, choices=ROLE_TYPE_CHOICES, default=UserRoleTypes.CLIENT, blank=True)
    phone = models.CharField(max_length=15, validators=[RegexValidator(r'\+375\((25|29|33|44)\)\d{7}', 'Invalid Phone Number')], blank=True)
    address = models.CharField(max_length=100, blank=True)
    date = models.DateField()   
    age = models.PositiveIntegerField()

    def __str__(self): return self.username 

class Climate(models.Model):
    winter = models.CharField(max_length=50)
    spring = models.CharField(max_length=50)
    summer = models.CharField(max_length=50)
    autumn = models.CharField(max_length=50)

    def __str__(self): return f'{ self.country.name } climate'

class Country(models.Model):
    name = models.CharField(max_length=30)
    climate = models.OneToOneField(Climate, on_delete=models.CASCADE, related_name='country')

    def __str__(self): return self.name

class Promocode(models.Model):
    value = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[a-zA-Z0-9]{10}$')])
    discount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    expires = models.DateTimeField()

    def float_value(self):
        return (100 - self.discount) / 100.0
    
    def is_valid(self):
        return self.expires > timezone.now() 
    
    def __str__(self):
        return self.value

class Hotel(models.Model):
    HOTEL_RATING_CHOICES = {
        HotelRatings.TERRIBLE: 1,
        HotelRatings.BAD: 2,
        HotelRatings.MEDIUM: 3,
        HotelRatings.GOOD: 4,
        HotelRatings.EXCELLENT: 5
    }

    name = models.CharField(max_length=30)
    stars = models.PositiveSmallIntegerField(choices=HOTEL_RATING_CHOICES, default=3)
    price_per_night = models.FloatField(validators=[MinValueValidator(0)])
    country = models.ForeignKey(Country, related_name='hotels', on_delete=models.CASCADE)

    def __str__(self): return self.name

class Trip(models.Model):
    TRIP_DURATION_CHOICES = {
        TripAvalableDurations.ONE_WEEK: 7,
        TripAvalableDurations.TWO_WEEKS: 14,
        TripAvalableDurations.FOUR_WEEKS: 28
    }

    hotel = models.ForeignKey(Hotel, related_name='trips', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='trips', on_delete=models.CASCADE)
    available = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=20)
    duration = models.PositiveSmallIntegerField(
        choices=TRIP_DURATION_CHOICES, default=TripAvalableDurations.ONE_WEEK)
    users = models.ManyToManyField(User, related_name='trips', blank=True)
    
    def price(self):
        return self.duration * self.hotel.price_per_night 
    
class Order(models.Model):
    amount = models.PositiveSmallIntegerField(default=1)
    promocode = models.ForeignKey(Promocode, blank=True, null=True, on_delete=models.SET_NULL)
    trip = models.ForeignKey(Trip, related_name='orders', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    departure = models.DateField()

    def price(self):
        price = self.trip.price()
        return price if self.promocode is None or not self.promocode.is_valid() else price * self.promocode.float_value()
    

class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

class PieceOfNews(models.Model):
    header = models.CharField(max_length=100)
    short_description = models.CharField(max_length=250)
    picture = models.ImageField(upload_to=DataStoringConfiguration.UPLOAD_IMAGES_TO)
    added = models.DateTimeField(auto_now_add=True)

class FAQ(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    added = models.DateField(auto_now_add=True)

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    picture = models.ImageField(upload_to=DataStoringConfiguration.UPLOAD_IMAGES_TO)

class Vacancy(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)

class Review(models.Model):
    name = models.CharField(max_length=30)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    text = models.CharField(max_length=250)
    written = models.DateField(auto_now_add=True)