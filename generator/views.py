from typing import Generator
from django.shortcuts import render
from django.http import HttpResponse
import random

# # Create your views here.
# def home(request):
#     return HttpResponse("Hello there friend!")

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    lenghth = int(request.GET.get("length", 12))    # 12 is the default length here
    
    if request.GET.get("uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get("specialcharacters"):
        characters.extend(list('!@#$%&*/|()'))
    if request.GET.get("numbers"):
        characters.extend(list('1234567890'))

    thepassword = ''
    for _ in range(lenghth):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})    