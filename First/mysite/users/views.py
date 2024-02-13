from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.


def index(request):
      return render(request, 'users/index.html')

def register(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f"Welcome {username}, your account has been created!")
    #         return redirect('food:home')
    # else:
    #     form = UserCreationForm()

    form = RegisterForm(request.POST or None)
    if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, your account has been created!")
            return redirect('users:login')
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
      return render(request, 'users/profile.html')