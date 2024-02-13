from django.shortcuts import redirect, render
from .models import Food, Consume, Goal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        food = Food.objects.get(name=food_consumed)
        consume = Consume(user=request.user, food_consumed=food)
        consume.save()

    food_items = Food.objects.all()
    consumed = Consume.objects.filter(user=request.user)
    total = {'carbs': 0, 'proteins': 0, 'fats': 0, 'calories': 0}
    for c in consumed:
        total['carbs'] += c.food_consumed.carbs
        total['proteins'] += c.food_consumed.proteins
        total['fats'] += c.food_consumed.fats
        total['calories'] += c.food_consumed.calories

    calorie_goal = request.GET.get('goal')
    percent = 0
    if calorie_goal != '' and calorie_goal is not None:
        request.user.goal.goal = int(calorie_goal)
        request.user.goal.save()
    if request.user.goal.goal!=0:
        percent = (total['calories']*100.0)/request.user.goal.goal
    percent = min(100.0, percent)

    total['carbs'] = format(total['carbs'], '.1f')
    total['proteins'] = format(total['proteins'], '.1f')
    total['fats'] = format(total['fats'], '.1f')
    percent = format(percent, '.2f')

    return render(request, 'myapp/index.html', {'food_items': food_items, 'consumed': consumed, 'total': total, 'calorie_percentage': percent})

@login_required
def delete_consume(request, id):
    consume = Consume.objects.get(pk=id)
    if request.method == "POST":
        consume.delete()
        return redirect('index')
    return render(request, 'myapp/delete.html')

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        Goal.objects.create(user=user)
        return redirect('login')
    return render(request, 'myapp/register.html', {'form': form})