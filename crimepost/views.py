from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from crimepost.models import Like, Dislike, Love, Comment, Reply, News, Views, ReadLater
import random

#ReadLater and also delete

    
    
def SaveNews(request):
    pk = request.POST.get("value")
    news = get_object_or_404(News, pk=pk)
    user_saving = request.user
    if ReadLater.objects.filter(news=news).exists():
        ReadLater.objects.get(news=news).delete()
        readlater = ReadLater.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("News Newly added")
    else:
        readlater = ReadLater.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("News added")
    
    
#View All save for later 
def ReadLaters(request):
    users = request.user
    read= ReadLater.objects.filter(name=users)
    context = {
        "read":read
    }
    return render(request, "News/ReadLater.htm", context)
    


#View All News
class Crime(ListView):
    template_name = "News/News.htm"
    paginate_by = 25
    context_object_name = "News"
    queryset = News.objects.all()

#Viewing A particular News
def CrimeView(request, title, headline, pk):
    neweview = get_object_or_404(News, pk=pk)
    neweview.views += 1
    neweview.save()
    newes = News.objects.all().exclude(pk=pk)
    neweis = random.sample(list(newes), min(len(list(newes)), 5))
    paginator = Paginator(neweis, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "News":neweview,
        "NewsRelated":neweis,
        "page_obj":page_obj
    }
    return render(request, "News/NewsDetail.htm", context)
    
    
    
    
    
    
    
    






