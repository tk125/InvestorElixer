from django.http        import HttpResponse
from django.shortcuts   import render, redirect

# Create your views here.

def index(request):
  return HttpResponse('<h1> Hello </h1>')

def email_sent(request):
    return render(request, 'email/sendemail.html')