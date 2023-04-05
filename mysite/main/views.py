from django.shortcuts import render


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


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
