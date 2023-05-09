from django.shortcuts import render


def home(request):
    args = {
        'title': 'Изучение английского',
        'navbar_list': ['Моё обучение', 'Форум', 'Карточки слов', 'Уроки', 'Другое']
    }
    return render(request, 'main/index.html', args)
