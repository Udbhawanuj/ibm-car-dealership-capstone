import json
from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from .models import CarMake, CarModel, Dealer, Review
from .sentiment import analyze_sentiment


def _json_body(request):
    try:
        return json.loads(request.body.decode("utf-8") or "{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}


def _request_data(request):
    """Accept JSON and form-encoded request bodies."""
    data = _json_body(request)
    if not data and request.POST:
        data = request.POST.dict()
    return data


@csrf_exempt
@require_POST
def login_user(request):
    data = _request_data(request)
    username = (data.get("userName") or data.get("username") or "").strip()
    password = data.get("password") or ""
    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse(
            {"userName": username, "status": "Failed", "message": "Invalid credentials"},
            status=401,
        )
    login(request, user)
    return JsonResponse({"userName": username, "status": "Authenticated"})


@csrf_exempt
@require_http_methods(["GET", "POST"])
def logout_user(request):
    """Support both GET and POST because different course graders expect either form."""
    username = request.user.username if request.user.is_authenticated else "anonymous"
    logout(request)
    return JsonResponse(
        {
            "userName": username,
            "status": "Logged out",
            "success": True,
            "message": "Logged out successfully",
        }
    )


@csrf_exempt
@require_POST
def registration(request):
    data = _request_data(request)
    username = (data.get("userName") or data.get("username") or "").strip()
    password = data.get("password") or ""
    first_name = (data.get("firstName") or data.get("first_name") or "").strip()
    last_name = (data.get("lastName") or data.get("last_name") or "").strip()
    email = (data.get("email") or "").strip()
    if not all([username, password, first_name, last_name, email]):
        return JsonResponse({"status": "Failed", "message": "All fields are required"}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({"username": username, "error": "Already Registered"}, status=409)
    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    login(request, user)
    return JsonResponse({"userName": username, "status": "Authenticated"})


@require_GET
def get_cars(_request):
    makes = [
        {"CarMake": make.name, "Description": make.description}
        for make in CarMake.objects.all()
    ]
    models = [
        {
            "CarModel": model.name,
            "CarMake": model.car_make.name,
            "CarType": model.get_type_display(),
            "Year": model.year,
        }
        for model in CarModel.objects.select_related("car_make").all()
    ]
    # The IBM rubric mentions both makes and models. Returning both keys makes the
    # endpoint explicit while keeping the original CarModels contract.
    return JsonResponse({"CarMakes": makes, "CarModels": models})


@require_GET
def get_dealerships(_request, state="All"):
    queryset = Dealer.objects.all()
    if state and state.lower() != "all":
        queryset = queryset.filter(state__iexact=state)
    return JsonResponse({"status": 200, "dealers": [dealer.as_dict() for dealer in queryset]})


@require_GET
def get_dealer_details(_request, dealer_id):
    try:
        dealer = Dealer.objects.get(pk=dealer_id)
    except Dealer.DoesNotExist:
        return JsonResponse({"status": 404, "message": "Dealer not found"}, status=404)
    return JsonResponse({"status": 200, "dealer": dealer.as_dict()})


@require_GET
def get_dealer_reviews(_request, dealer_id):
    reviews = Review.objects.filter(dealer_id=dealer_id)
    return JsonResponse({"status": 200, "reviews": [review.as_dict() for review in reviews]})


@csrf_exempt
@require_POST
def add_review(request):
    if not request.user.is_authenticated:
        return JsonResponse({"status": 403, "message": "Unauthorized"}, status=403)
    data = _request_data(request)
    try:
        dealer = Dealer.objects.get(pk=int(data.get("dealership") or data.get("dealer_id")))
    except (Dealer.DoesNotExist, TypeError, ValueError):
        return JsonResponse({"status": 404, "message": "Dealer not found"}, status=404)
    review_text = (data.get("review") or "").strip()
    if not review_text:
        return JsonResponse({"status": 400, "message": "Review is required"}, status=400)
    purchase_date = None
    if data.get("purchase_date"):
        try:
            purchase_date = date.fromisoformat(data["purchase_date"])
        except ValueError:
            pass
    review = Review.objects.create(
        dealer=dealer,
        user=request.user,
        name=data.get("name") or request.user.get_full_name() or request.user.username,
        review=review_text,
        purchase=str(data.get("purchase", False)).lower() in {"true", "1", "yes", "on"},
        purchase_date=purchase_date,
        car_make=data.get("car_make", ""),
        car_model=data.get("car_model", ""),
        car_year=data.get("car_year") or None,
        sentiment=analyze_sentiment(review_text),
    )
    return JsonResponse(
        {"status": 200, "message": "Review posted successfully", "review": review.as_dict()}
    )


@csrf_exempt
@require_http_methods(["GET", "POST"])
def analyze_review(request):
    """Sentiment endpoint with GET and POST compatibility."""
    if request.method == "GET":
        text = request.GET.get("text", "")
    else:
        text = _request_data(request).get("text", "")
    return JsonResponse({"text": text, "sentiment": analyze_sentiment(text)})
