from django.shortcuts import render


def home(request):
    args = {
        'title': 'Изучение английского'
    }
    return render(request, 'main/index.html', args)
