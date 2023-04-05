from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def main(request):
    data = {
        'title': 'Главная страница',
        'values': ['First', 'second', 'third'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'programming'
        }
    }
    return render(request, 'main/main.html', data)


@login_required(login_url='/login/')
def about(request):
    return render(request, 'main/about.html')


@login_required(login_url='/login/')
def contacts(request):
    return render(request, 'main/contacts.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('/')
