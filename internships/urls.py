from django.urls import path
from . import views
from .views import start_scraping, get_internships

urlpatterns = [
    path('', views.home, name='home'),
    path('start_scraping/', start_scraping, name='start_scraping'),
    path('get_internships/', get_internships, name='get_internships'),
]