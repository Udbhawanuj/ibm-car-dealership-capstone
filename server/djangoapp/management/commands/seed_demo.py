from datetime import date
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from djangoapp.models import CarMake, CarModel, Dealer, Review
from djangoapp.sentiment import analyze_sentiment


DEALERS = [
    ('Best Cars Dealership', 'Best Cars', '1200 Main Street', 'Kansas City', 'KS', '66101', '39.114053', '-94.627464', '+1 913-555-0101'),
    ('Lone Star Auto Plaza', 'Lone Star', '880 Congress Avenue', 'Austin', 'TX', '78701', '30.267153', '-97.743057', '+1 512-555-0112'),
    ('Pacific Motor Gallery', 'Pacific Motor', '450 Market Street', 'San Francisco', 'CA', '94105', '37.789800', '-122.394200', '+1 415-555-0130'),
    ('Empire Auto Center', 'Empire Auto', '275 Madison Avenue', 'New York', 'NY', '10016', '40.748400', '-73.985700', '+1 212-555-0144'),
    ('Sunflower Motors Wichita', 'Sunflower', '900 East Douglas Avenue', 'Wichita', 'KS', '67202', '37.686981', '-97.335579', '+1 316-555-0165'),
    ('Windy City Cars', 'Windy City', '333 North Michigan Avenue', 'Chicago', 'IL', '60601', '41.887400', '-87.624800', '+1 312-555-0170'),
    ('Bay State Automotive', 'Bay State', '100 Summer Street', 'Boston', 'MA', '02110', '42.354300', '-71.058800', '+1 617-555-0188'),
    ('Evergreen Auto House', 'Evergreen', '1400 4th Avenue', 'Seattle', 'WA', '98101', '47.609700', '-122.333100', '+1 206-555-0192'),
    ('Sunshine Car Hub', 'Sunshine Hub', '200 Biscayne Boulevard', 'Miami', 'FL', '33131', '25.771900', '-80.191000', '+1 305-555-0124'),
]

MAKES = {
    'Toyota': [('Camry', 'SEDAN', 2024), ('RAV4', 'SUV', 2024), ('Corolla', 'SEDAN', 2023)],
    'Honda': [('Civic', 'SEDAN', 2024), ('CR-V', 'SUV', 2024), ('Accord', 'SEDAN', 2023)],
    'Ford': [('F-150', 'PICKUP', 2024), ('Mustang', 'COUPE', 2024), ('Explorer', 'SUV', 2023)],
    'Tesla': [('Model 3', 'SEDAN', 2024), ('Model Y', 'SUV', 2024)],
    'BMW': [('3 Series', 'SEDAN', 2024), ('X5', 'SUV', 2024)],
}

REVIEWS = [
    (1, 'Maya Johnson', 'Fantastic services. The sales team was friendly, transparent, and very professional.', True, 'Toyota', 'Camry', 2024),
    (1, 'Ethan Clark', 'Great experience from the first test drive to final paperwork. I would recommend this branch.', True, 'Honda', 'CR-V', 2023),
    (1, 'Olivia Martin', 'The showroom was clean and the service advisor explained every cost clearly.', False, '', '', None),
    (2, 'Noah Williams', 'Helpful staff and a smooth purchase process.', True, 'Ford', 'F-150', 2024),
    (3, 'Ava Lee', 'Good selection and honest communication throughout the visit.', False, '', '', None),
]


class Command(BaseCommand):
    help = 'Create deterministic demo users, cars, dealers, and reviews.'

    def handle(self, *args, **options):
        root, _ = User.objects.get_or_create(username='root', defaults={'email': 'root@drivesphere.example', 'is_staff': True, 'is_superuser': True})
        root.is_staff = True
        root.is_superuser = True
        root.set_password('Root@123')
        root.save()

        reviewer, _ = User.objects.get_or_create(username='reviewer', defaults={'first_name': 'Udbhaw', 'last_name': 'Reviewer', 'email': 'reviewer@drivesphere.example'})
        reviewer.first_name = 'Udbhaw'
        reviewer.last_name = 'Reviewer'
        reviewer.email = 'reviewer@drivesphere.example'
        reviewer.set_password('Reviewer@123')
        reviewer.save()

        for make_name, models in MAKES.items():
            make, _ = CarMake.objects.get_or_create(name=make_name, defaults={'description': f'{make_name} passenger vehicles'})
            for model_name, car_type, year in models:
                CarModel.objects.get_or_create(car_make=make, name=model_name, year=year, defaults={'type': car_type})

        for item in DEALERS:
            Dealer.objects.get_or_create(
                full_name=item[0],
                defaults={'short_name': item[1], 'address': item[2], 'city': item[3], 'state': item[4], 'zip_code': item[5], 'latitude': item[6], 'longitude': item[7], 'phone': item[8]},
            )

        if Review.objects.count() == 0:
            for dealer_id, name, text, purchase, make, model, year in REVIEWS:
                Review.objects.create(
                    dealer_id=dealer_id,
                    user=reviewer,
                    name=name,
                    review=text,
                    purchase=purchase,
                    purchase_date=date(2026, 6, 20) if purchase else None,
                    car_make=make,
                    car_model=model,
                    car_year=year,
                    sentiment=analyze_sentiment(text),
                )

        self.stdout.write(self.style.SUCCESS('Demo data ready: root/reviewer users, dealers, cars, and reviews.'))
