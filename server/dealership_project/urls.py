from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.http import JsonResponse
from django.contrib.staticfiles.storage import staticfiles_storage


def health(_request):
    return JsonResponse({'status': 'ok', 'service': 'DriveSphere'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health, name='health'),
    path('djangoapp/', include('djangoapp.urls')),
    path('', include('djangoapp.page_urls')),
    path('about/', RedirectView.as_view(url='/static/About.html', permanent=False)),
    path('contact/', RedirectView.as_view(url='/static/Contact.html', permanent=False)),
]
