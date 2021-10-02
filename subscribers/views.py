from django.shortcuts import render
from django.http import HttpResponse
from subscribers.models import NewsLetter
# Create your views here.
def NewsLetters(request):
    newsletterinput = request.POST.get("value")
    if NewsLetter.objects.filter(email=newsletterinput).exists():
        return HttpResponse("Email Already Registered With Crimeheist")
    else:
        news = NewsLetter(email=newsletterinput)
        news.save()
        return HttpResponse("Email Added To Crimeheist NewsLetter")
    
    
