from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.
def index(request):

    context = {
        'title': 'Home - Main',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'content': 'About us',
        'text_on_page': 'Text text text text'
    }

    return render(request, 'main/about.html', context)