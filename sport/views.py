from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from sport.models import Like, Dislike, Love, Somment, Seply, Sport, Views, ReadLaterSport
import random
#Replying Views to comment 
def SportReply(request):
    print(request.user)
    posts = request.POST.get("post")
    messages = request.POST.get("content")
    userc = request.user
    postes = get_object_or_404(Somment,pk=posts)
    commentsave = Seply(name=request.user, content=messages, commenties=postes)
    commentsave.save()
    return redirect("sport:seplyview" ,pk=postes.pk)
#Reply Views
def SeplyView(request, pk):
    seplys = get_object_or_404(Somment, pk=pk)
    seplyis = Seply.objects.filter(commenties=seplys)
    context = {
        "comment":seplys,
        "replys":seplyis
    }
    return render(request, "Sport/SportReply.htm", context)


#Getting All Cment for post
def SportCommentAll(request, pk):
    post = get_object_or_404(Sport, pk=pk)
    comments = Somment.objects.all().filter(post=post, is_approved=True)
    return JsonResponse({
        "comment":list(comments.values())
    })
    
    
    

#Comment For Sport News
def SportComment(request):
    print(request.user)
    posts = request.POST.get("post")
    messages = request.POST.get("content")
    userc = request.user
    postes = get_object_or_404(Sport,pk=posts)
    commentsave = Somment(names=request.user, content=messages, post=postes)
    commentsave.save()
    return redirect("sport:sportview" ,title=postes.title ,headline=postes.headline ,pk=postes.pk)
    
    
    
    
    
#ReadLaterSport and also delete
def SaveSport(request):
    pk = request.POST.get("value")
    news = get_object_or_404(Sport, pk=pk)
    user_saving = request.user
    if ReadLaterSport.objects.filter(news=news).exists():
        ReadLaterSport.objects.get(news=news).delete()
        readlater = ReadLaterSport.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("Sport News  Newly added")
    else:
        readlater = ReadLaterSport.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("Sport News added")
    
    
#View All save for later 
def ReadLater(request):
    users = request.user
    read= ReadLaterSport.objects.filter(name=users)
    context = {
        "read":read
    }
    return render(request, "Sport/ReadLaterSport.htm", context)
    


#View All Sport
class Sports(ListView):
    template_name = "Sport/Sport.htm"
    paginate_by = 25
    context_object_name = "Sport"
    queryset = Sport.objects.all()

#Viewing A particular Sport
def SportView(request, title, headline, pk):
    neweview = get_object_or_404(Sport, pk=pk)
    neweview.views += 1
    neweview.save()
    comments = Somment.objects.filter(post=neweview)
    comment = int(Somment.objects.filter(post=neweview).count())
    newes = Sport.objects.all().exclude(pk=pk)
    neweis = random.sample(list(newes), min(len(list(newes)), 5))
    paginator = Paginator(neweis, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(int(comment))
    context = {
        "Sport":neweview,
        "SportRelated":neweis,
        "page_obj":page_obj,
        "comments":comments,
        "commentcount":comment
    }
    return render(request, "Sport/SportDetail.htm", context)
    
    
    
    
    
    
    
    






