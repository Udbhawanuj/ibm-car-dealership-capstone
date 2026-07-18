from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
        ('MINIVAN', 'Minivan'),
        ('CONVERTIBLE', 'Convertible'),
        ('PICKUP', 'Pickup'),
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2024,
        validators=[MinValueValidator(2015), MaxValueValidator(2030)],
    )

    class Meta:
        ordering = ['car_make__name', 'name']
        unique_together = ('car_make', 'name', 'year')

    def __str__(self):
        return f'{self.car_make.name} {self.name} ({self.year})'


class Dealer(models.Model):
    full_name = models.CharField(max_length=180)
    short_name = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    phone = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.full_name

    def as_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'short_name': self.short_name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip': self.zip_code,
            'lat': float(self.latitude),
            'long': float(self.longitude),
            'phone': self.phone,
        }


class Review(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    review = models.TextField()
    purchase = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    car_make = models.CharField(max_length=100, blank=True)
    car_model = models.CharField(max_length=100, blank=True)
    car_year = models.IntegerField(null=True, blank=True)
    sentiment = models.CharField(max_length=16, default='neutral')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return f'Review by {self.name} for {self.dealer.short_name}'

    def as_dict(self):
        return {
            'id': self.id,
            'dealership': self.dealer_id,
            'name': self.name,
            'review': self.review,
            'purchase': self.purchase,
            'purchase_date': self.purchase_date.isoformat() if self.purchase_date else None,
            'car_make': self.car_make,
            'car_model': self.car_model,
            'car_year': self.car_year,
            'sentiment': self.sentiment,
        }
