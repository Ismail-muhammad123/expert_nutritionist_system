from django.contrib import admin

from nutrition_schedule.models import FoodItem

# Register your models here.


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "unit", "calories"]
