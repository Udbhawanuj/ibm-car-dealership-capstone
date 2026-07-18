from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import CarMake, Dealer, Review
from .sentiment import analyze_sentiment


STATES = [
    ('All', 'All States'), ('CA', 'California'), ('FL', 'Florida'),
    ('IL', 'Illinois'), ('KS', 'Kansas'), ('MA', 'Massachusetts'),
    ('NY', 'New York'), ('TX', 'Texas'), ('WA', 'Washington'),
]


def home(request, state='All'):
    queryset = Dealer.objects.all()
    selected_state = state.upper()
    if selected_state != 'ALL':
        queryset = queryset.filter(state__iexact=selected_state)
    return render(request, 'djangoapp/home.html', {
        'dealers': queryset,
        'states': STATES,
        'selected_state': selected_state,
    })


def dealer_detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    return render(request, 'djangoapp/dealer_detail.html', {
        'dealer': dealer,
        'reviews': dealer.reviews.all(),
    })


def review_form(request, dealer_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Please log in before posting a review.')
        return redirect('/')
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    return render(request, 'djangoapp/review_form.html', {
        'dealer': dealer,
        'makes': CarMake.objects.prefetch_related('models').all(),
    })


def register_page(request):
    return render(request, 'djangoapp/register.html')


@require_POST
def ui_login(request):
    user = authenticate(
        request,
        username=request.POST.get('username', ''),
        password=request.POST.get('password', ''),
    )
    if user:
        login(request, user)
        messages.success(request, f'Welcome back, {user.username}!')
    else:
        messages.error(request, 'Invalid username or password.')
    return redirect(request.POST.get('next') or '/')


@require_POST
def ui_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/')


@require_POST
def ui_register(request):
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    if any(not request.POST.get(field, '').strip() for field in fields):
        messages.error(request, 'Please complete every registration field.')
        return redirect('/register/')
    username = request.POST['username'].strip()
    if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is already registered.')
        return redirect('/register/')
    user = User.objects.create_user(
        username=username,
        password=request.POST['password'],
        first_name=request.POST['first_name'].strip(),
        last_name=request.POST['last_name'].strip(),
        email=request.POST['email'].strip(),
    )
    login(request, user)
    messages.success(request, f'Account created. Welcome, {username}!')
    return redirect('/')


@require_POST
def ui_add_review(request, dealer_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Please log in before posting a review.')
        return redirect('/')
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    review_text = request.POST.get('review', '').strip()
    if not review_text:
        messages.error(request, 'Review text is required.')
        return redirect(f'/dealer/{dealer_id}/review/')
    Review.objects.create(
        dealer=dealer,
        user=request.user,
        name=request.user.get_full_name() or request.user.username,
        review=review_text,
        purchase=request.POST.get('purchase') == 'on',
        purchase_date=request.POST.get('purchase_date') or None,
        car_make=request.POST.get('car_make', ''),
        car_model=request.POST.get('car_model', ''),
        car_year=request.POST.get('car_year') or None,
        sentiment=analyze_sentiment(review_text),
    )
    messages.success(request, 'Your review was posted successfully and appears first below.')
    return redirect(f'/dealer/{dealer_id}/')
