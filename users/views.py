from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SingUpForm


def singUp(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form = SingUpForm()

    return render(request, 'users/register.html', context={'form': form})


def logOut(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def ProfileInfo(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})





