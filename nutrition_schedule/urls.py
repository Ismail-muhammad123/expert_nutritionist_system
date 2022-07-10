from django.urls import path
# from .views import create_foods, get_diet_schedule
from .views import get_diet_schedule, index


urlpatterns = [
    path('result', get_diet_schedule, name='results_page'),
    path('', index, name='home_page'),
    # path('initiate', create_foods),
]
