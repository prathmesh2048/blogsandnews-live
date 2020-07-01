from django.shortcuts import render
import simplejson
import requests


def business_news(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api = simplejson.loads(news_api_request.content)
    context = {
        'api': api
    }
    template = 'newsapp/business_news.html'
    return render(request, template, context)


def news_list(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api = simplejson.loads(news_api_request.content)
    context = {
        'api': api
    }
    template = 'newsapp/news.html'
    return render(request, template, context)


def sports_news(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api = simplejson.loads(news_api_request.content)
    context = {
        'api': api
    }
    template = 'newsapp/sports_news.html'
    return render(request, template, context)


def tech_news(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api = simplejson.loads(news_api_request.content)
    context = {
        'api': api
    }
    template = 'newsapp/tech_news.html'
    return render(request, template, context)


def entertainment_news(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api = simplejson.loads(news_api_request.content)
    context = {
        'api': api
    }
    template = 'newsapp/entertainment_news.html'
    return render(request, template, context)


def health_news(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api = simplejson.loads(news_api_request.content)
    context = {
        'api': api
    }
    template = 'newsapp/health_news.html'
    return render(request, template, context)


def science_news(request):
    news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api = simplejson.loads(news_api_request.content)
    context = {
        'api': api
    }
    template = 'newsapp/science_news.html'
    return render(request, template, context)


def international_news(request):
    news_api_request = requests.get('http://newsapi.org/v2/everything?q=bitcoin&from=2020-05-30&sortBy=publishedAt&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api = simplejson.loads(news_api_request.content)
    news_api_request2 = requests.get('http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api2 = simplejson.loads(news_api_request2.content)
    news_api_request3 = requests.get('http://newsapi.org/v2/everything?q=apple&from=2020-06-28&to=2020-06-28&sortBy=popularity&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api3 = simplejson.loads(news_api_request3.content)
    news_api_request4 = requests.get('http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api4 = simplejson.loads(news_api_request4.content)
    news_api_request5 = requests.get('http://newsapi.org/v2/everything?domains=wsj.com&apiKey=cc35aaa7e3b54248970983cb40291f59')
    api5 = simplejson.loads(news_api_request5.content)

    context = {
        'api': api,
        'api2': api2,
        'api3': api3,
        'api4': api4,
        'api5': api5,

    }
    template = 'newsapp/international_news.html'
    return render(request, template, context)