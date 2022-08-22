from django.urls import path
# from .views import create_foods, get_diet_schedule
from .views import about, get_diet_schedule, index, search, guide


urlpatterns = [
    path('', index, name='home_page'),
    path('search', search, name='search_page'),
    path('result', get_diet_schedule, name='results_page'),
    path('about', about, name='about_page'),
    path('guide', guide, name='guide_page'),
]
