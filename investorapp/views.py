from django.http        import HttpResponse
from django.shortcuts   import render, redirect
from .models import *
from .yahoofinance import *
import csv

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

import re
def fiveYearSummary(request):
  #!/usr/bin/python

  # Open a file
  fo = open("csv/hawpar2009-2005.csv", "r+")
  print ("Name of the file: ", fo.name)

  lines = fo.readlines()

  with open("csv/new.csv", mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for line in lines:
      line=line.replace(',', '').replace('\n', '').replace('\r', '') # Earnings (EBIT) 2,548.5 2,086.6 2,190.8 2,258.6 2,436.9

      digit_pos=findDigitPos(line)
      if(digit_pos!=0): # Earnings (EBIT) 2548.5 2086.6 2190.8 2258.6 2436.9 ->Earnings (EBIT) ,2548.5,2086.6,2190.8,2258.6,2436.9
        figures=line[digit_pos:].replace(' ', ',')
        line= line[0: digit_pos] + ',' + figures
      print(line+'\n')
      csv_writer.writerow(line.split (","))

  # Close opend file
  fo.close()
  return HttpResponse('<h1> All Stock Prices Refreshed </h1>')

def findDigitPos(s1):
  m = re.search(r"(\d|((-\d)|(- \d))|[(](\d| \d))", s1) # '9', '-9', '- 9', '( 9 )', '(9)
  if m is not None:
    print("Digit found at position", m.start())
    return m.start()
  else:
    print("No digit in that string")
    return 0

