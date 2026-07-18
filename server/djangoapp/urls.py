from django.urls import path

from . import views

app_name = "djangoapp"

urlpatterns = [
    path("register", views.registration, name="register"),
    path("register/", views.registration),
    path("login", views.login_user, name="login"),
    path("login/", views.login_user),
    path("logout", views.logout_user, name="logout_no_slash"),
    path("logout/", views.logout_user, name="logout"),
    path("get_cars", views.get_cars, name="getcars"),
    path("get_cars/", views.get_cars),
    path("get_dealers/", views.get_dealerships, name="get_dealers"),
    path("get_dealers/<str:state>", views.get_dealerships, name="get_dealers_by_state"),
    path("get_dealers/<str:state>/", views.get_dealerships),
    path("dealer/<int:dealer_id>", views.get_dealer_details, name="dealer_details"),
    path("dealer/<int:dealer_id>/", views.get_dealer_details),
    path("reviews/dealer/<int:dealer_id>", views.get_dealer_reviews, name="dealer_reviews"),
    path("reviews/dealer/<int:dealer_id>/", views.get_dealer_reviews),
    path("add_review", views.add_review, name="add_review"),
    path("add_review/", views.add_review),
    # Both spellings are supported because course versions use different names.
    path("analyze_review", views.analyze_review, name="analyze_review"),
    path("analyze_review/", views.analyze_review),
    path("analyzeReview", views.analyze_review, name="analyze_review_camel"),
    path("analyzeReview/", views.analyze_review),
]
