from django.shortcuts import render
from .models import News, Crossing
from django.template import loader
# Create your views here.

from django.http import HttpResponse


def news(request):
    news_list = News.objects.order_by('-updated_at')
    template = loader.get_template('info/news.html')
    context = {
        'news_list': news_list,
    }
    return HttpResponse(template.render(context, request))

def crossings(request):
    crossings_list = Crossing.objects.order_by('order')
    # template = loader.get_template('base.html')
    template = loader.get_template('info/crossings.html')
    context = {
        'crossings_list': crossings_list,
    }
    return HttpResponse(template.render(context, request))