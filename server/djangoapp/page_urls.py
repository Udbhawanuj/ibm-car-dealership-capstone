from django.urls import path
from . import page_views

urlpatterns = [
    path('', page_views.home, name='home'),
    path('dealers/<str:state>/', page_views.home, name='dealers_by_state_page'),
    path('dealer/<int:dealer_id>/', page_views.dealer_detail, name='dealer_detail_page'),
    path('dealer/<int:dealer_id>/review/', page_views.review_form, name='review_form'),
    path('register/', page_views.register_page, name='register_page'),
    path('ui/login/', page_views.ui_login, name='ui_login'),
    path('ui/logout/', page_views.ui_logout, name='ui_logout'),
    path('ui/register/', page_views.ui_register, name='ui_register'),
    path('ui/add-review/<int:dealer_id>/', page_views.ui_add_review, name='ui_add_review'),
]
