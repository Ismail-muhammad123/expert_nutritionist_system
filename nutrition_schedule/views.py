from multiprocessing import context
from random import Random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from numpy import require
from .models import FoodItem
# from django.templatetags.static import static

# Create your views here.


def get_age_stage(age):
    age = eval(age)
    if age >= 2 and age <= 4:
        return 'todler'
    elif age >= 5 and age <= 12:
        return 'infant'
    elif age >= 13 and age <= 19:
        return 'teen'


def get_required_calories(gender, age_stage, activity_level):
    """
        gender:
            - male
            - female
        age:
            Integer
        age_stage:
            age 1-4 => todler,
            age 5-12 => infant
            age 13-18 => teen
        activity levels:
            1 => low activity
            2 => moderately active
            3 => very active
    """
    activity_level = eval(activity_level)
    if gender.lower() == 'male':
        # male todler
        if age_stage.lower() == 'todler':
            if activity_level == 1:
                return (1000, 1200)
            elif activity_level == 2:
                return (1000, 1400)
            elif activity_level == 3:
                return (1000, 1400)
        # male infant
        elif age_stage.lower() == 'infant':
            if activity_level == 1:
                return (1200, 1400)
            elif activity_level == 2:
                return (1400, 1600)
            elif activity_level == 3:
                return (1600, 2000)
        # male teen
        elif age_stage.lower() == 'teen':
            if activity_level == 1:
                return (2000, 2400)
            elif activity_level == 2:
                return (2400, 2800)
            elif activity_level == 3:
                return (2800, 3200)

    elif gender.lower() == 'female':
        # female todler
        if age_stage.lower() == 'todler':
            if activity_level == 1:
                return (1000, )
            elif activity_level == 2:
                return (1000, 1200)
            elif activity_level == 3:
                return (1000, 1400)
        # female infant
        elif age_stage.lower() == 'infant':
            if activity_level == 1:
                return (1200, 1400)
            elif activity_level == 2:
                return (1400, 1600)
            elif activity_level == 3:
                return (1400, 1800)
        # female teen
        elif age_stage.lower() == 'teen':
            if activity_level == 1:
                return (1800, )
            elif activity_level == 2:
                return (2000,)
            elif activity_level == 3:
                return (2400, )


def get_diet_schedule(request):
    age = request.GET.get('age', None)
    activity_level = request.GET.get('activity_level', None)
    gender = request.GET.get('gender', None)

    if gender == None or age == None or activity_level == None:
        return redirect('home_page')

    if eval(age) < 2:
        return redirect('home_page')

    age_stage = get_age_stage(age)

    required_calories = get_required_calories(
        gender, age_stage, activity_level)

    food_items = list(FoodItem.objects.all())

    context = {
        "food_items": []
    }

    rand = Random()

    total_calories = 0

    if len(required_calories) == 1:
        while total_calories < required_calories[0]:
            item = rand.choice(food_items)
            context['food_items'].append(
                food_items.pop(food_items.index(item)))
            total_calories += item.calories
    elif len(required_calories) == 2:
        while total_calories <= required_calories[1]:
            item = rand.choice(food_items)
            if (total_calories + item.calories) < required_calories[1]:
                context['food_items'].append(
                    food_items.pop(food_items.index(item)))
                total_calories += item.calories
            else:
                break

    context['total_calories'] = total_calories
    context['gender'] = gender
    context['age'] = age
    context['activity_level'] = activity_level
    context['min_required_calories'] = required_calories[0]
    context['max_required_calories'] = required_calories[1] if len(
        required_calories) == 2 else "none"

    return render(request, 'nutrition_schedule/result.html', context=context)


def index(request):
    return render(request, 'nutrition_schedule/home.html')

# def create_foods(request):
#     # file = open(static('nutrients_csvfile.csv'))
#     file = open('nutrition_schedule/static/nutrients_csvfile.csv')
#     for index, line in enumerate(file.readlines()):
#         print("[creating Item {}".format(index))
#         try:
#             food, measure, calories, category = line.split(",")
#         except:
#             continue

#         if calories == "":
#             continue

#         calories = eval(calories)

#         try:
#             obj = FoodItem(name=food, calories=calories,
#                            unit=measure, category=category)
#             obj.save()
#         except:
#             continue
#     return redirect('/')
