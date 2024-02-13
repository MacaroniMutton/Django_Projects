from django.contrib import admin
from .models import Food, Consume, Goal
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'carbs', 'proteins', 'fats', 'calories',)

admin.site.register(Food, FoodAdmin)
admin.site.register(Consume)
admin.site.register(Goal)