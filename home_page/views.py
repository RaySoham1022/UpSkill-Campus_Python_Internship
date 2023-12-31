from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import pyshorteners


def index(request, **kwargs):
    if request.user.is_authenticated == True:
        present_user = request.user.username 
        if request.method == 'POST':
            try:
                link = request.POST.get('longurl')
                name = request.POST.get('urlname')
                shortener = pyshorteners.Shortener()
                finalurl = shortener.tinyurl.short(link)
                shorturlvalue = finalurl
                data = {'shorturlvalue':shorturlvalue}
                URLRedirection(profile_username = present_user,urlname = name, shortURL = finalurl, longURL =link ).save()
                return render(request, "index.html", data)
            except:
                shorturlvalue = ""
                data = {'shorturlvalue':shorturlvalue}
                return render(request, "index.html", data)
        else:
            shorturlvalue = ""
            data = {'shorturlvalue':shorturlvalue}
            return render(request, "index.html", data)
    else:
        if request.method == 'POST':
            try:
                link = request.POST.get('longurl')
                shortener = pyshorteners.Shortener()
                finalurl = shortener.tinyurl.short(link)
                shorturlvalue = finalurl
                data = {'shorturlvalue':shorturlvalue}
                return render(request, "index.html", data)
            except:
                shorturlvalue = ""
                data = {'shorturlvalue':shorturlvalue}
                return render(request, "index.html", data)
        else:
            shorturlvalue = ""
            data = {'shorturlvalue':shorturlvalue}
            return render(request, "index.html", data)

def myurls(request):
    if request.user.is_authenticated == True:
        present_user = request.user.username
        urldetails = URLRedirection.objects.filter(profile_username = present_user)
        data = {'urldetails' : urldetails}
        return render(request, 'myurls.html',data)
    else:
        return redirect('/authenticate/login')