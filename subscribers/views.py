from django.shortcuts import render, redirect
from django.http import HttpResponse
from subscribers.models import NewsLetter
# Create your views here.
def Unsub1(request):
    if NewsLetter.objects.filter(email=request.user.email).exists():
        newsletter = NewsLetter.objects.get(email=request.user.email)
    else:
        newsletter = NewsLetter.objects.create(email=request.user.email)
        newsletter.save()
        newsletter = NewsLetter.objects.get(email=request.user.email)
    context = {
        "newletter":newsletter
    }
    return render(request, "Subscribe/Unsub1.htm", context)
    
def Unsub2(request, pk):
    newletter = NewsLetter.objects.get(pk=pk)
    newletter.delete()
    return redirect("account:setting")

def NewsLetters(request):
    newsletterinput = request.POST.get("value")
    if NewsLetter.objects.filter(email=newsletterinput).exists():
        return HttpResponse("Email Already Registered With Crimeheist")
    else:
        news = NewsLetter.objects.create(email=newsletterinput)
        
        return HttpResponse("Email Added To Crimeheist NewsLetter")
    
    
