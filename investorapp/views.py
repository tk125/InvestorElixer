from django.http        import HttpResponse
from django.shortcuts   import render, redirect
from .models import *
from .yahoofinance import *

# Create your views here.

def index(request):
  return HttpResponse('<h1> Index Page </h1>')

def email_sent(request):
    return render(request, 'email/sendemail.html')

def refreshAllStockPrice(request):
  stocks=Stock.objects.all()
  for stock in stocks:
    ticker_with_si=stock.ticker+".SI"
    res=(parse(ticker_with_si))
    print(res)
  return HttpResponse('<h1> All Stock Prices Refreshed </h1>')
