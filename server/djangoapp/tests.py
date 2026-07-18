import json

from django.contrib.auth.models import User
from django.test import TestCase

from djangoapp.models import CarMake, CarModel, Dealer


class DealershipApiTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="tester", password="TestPass123")
        cls.dealer = Dealer.objects.create(
            full_name="Test Dealer",
            short_name="Test",
            address="1 Main St",
            city="Wichita",
            state="KS",
            zip_code="67202",
        )
        make = CarMake.objects.create(name="TestMake", description="Test cars")
        CarModel.objects.create(car_make=make, name="TestModel", type="SUV", year=2024)

    def test_dealer_list(self):
        response = self.client.get("/djangoapp/get_dealers/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["dealers"][0]["state"], "KS")

    def test_login_and_get_logout(self):
        login_response = self.client.post(
            "/djangoapp/login",
            data=json.dumps({"userName": "tester", "password": "TestPass123"}),
            content_type="application/json",
        )
        self.assertEqual(login_response.status_code, 200)
        self.assertEqual(login_response.json()["status"], "Authenticated")
        logout_response = self.client.get("/djangoapp/logout/")
        self.assertEqual(logout_response.status_code, 200)
        self.assertEqual(logout_response.json()["userName"], "tester")
        self.assertEqual(logout_response.json()["status"], "Logged out")

    def test_sentiment_get_and_post_alias(self):
        get_response = self.client.get("/djangoapp/analyze_review?text=Fantastic%20services")
        self.assertEqual(get_response.json()["sentiment"], "positive")
        post_response = self.client.post(
            "/djangoapp/analyzeReview/",
            data=json.dumps({"text": "Fantastic services"}),
            content_type="application/json",
        )
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(post_response.json()["sentiment"], "positive")

    def test_cars_returns_makes_and_models(self):
        response = self.client.get("/djangoapp/get_cars")
        payload = response.json()
        self.assertIn("CarMakes", payload)
        self.assertIn("CarModels", payload)
        self.assertEqual(payload["CarModels"][0]["CarMake"], "TestMake")
