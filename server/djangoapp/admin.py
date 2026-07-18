from django.contrib import admin
from .models import CarMake, CarModel, Dealer, Review


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name')


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'city', 'state', 'phone')
    list_filter = ('state',)
    search_fields = ('full_name', 'city', 'state')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'dealer', 'sentiment', 'purchase', 'created_at')
    list_filter = ('sentiment', 'purchase', 'dealer__state')
    search_fields = ('name', 'review', 'dealer__full_name')
