from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from entertain.models import Eomment, Entertain, ReadLaterEntertain, EntertainCate
import random
#Replying Views to comment 
def EntertainCategory1(request, pk):
    category = Entertain.objects.filter(category=pk)
    paginator = Paginator(category, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "Entertain":category,
        "page_obj":page_obj
    }
    return render(request, "Entertain/EntertainCate.htm", context)

#Getting All Cment for post
def EntertainCommentAll(request, pk):
    post = get_object_or_404(Entertain, pk=pk)
    comments = Eomment.objects.all().filter(post=post, is_approved=True)
    return JsonResponse({
        "comment":list(comments.values())
    })
    
    
    

#Comment For Entertain News
def EntertainComment(request):
    print(request.user)
    posts = request.POST.get("post")
    messages = request.POST.get("content")
    userc = request.user
    postes = get_object_or_404(Entertain,pk=posts)
    commentsave = Eomment(names=request.user, content=messages, post=postes)
    commentsave.save()
    return redirect("entertain:entertainview" ,title=postes.title ,headline=postes.headline ,pk=postes.pk)
    
    
    
    
    
#ReadLaterEntertain and also delete
def SaveEntertain(request):
    pk = request.POST.get("value")
    news = get_object_or_404(Entertain, pk=pk)
    user_saving = request.user
    if ReadLaterEntertain.objects.filter(news=news).exists():
        ReadLaterEntertain.objects.get(news=news).delete()
        readlater = ReadLaterEntertain.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("Entertain News  Newly added")
    else:
        readlater = ReadLaterEntertain.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("Entertain News added")
    
    
#View All save for later 
def ReadLater(request):
    users = request.user
    read= ReadLaterEntertain.objects.filter(name=users)
    context = {
        "read":read
    }
    return render(request, "Entertain/ReadLaterEntertain.htm", context)
    


#View All Entertain Entertain category
def Entertains(request):
    category = EntertainCate.objects.all()
    sports = Entertain.objects.all()
    paginator = Paginator(sports, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "Entertain":sports,
        "category":category,
        "page_obj":page_obj
    }
    return render(request, "Entertain/Entertain.htm", context)


#class Entertains(ListView):
   # template_name = "Entertain/Entertain.htm"
   # paginate_by = 25
   # context_object_name = "Entertain"
   # queryset = Entertain.objects.all()

#Viewing A particular Entertain
def EntertainView(request, title, headline, pk):
    neweview = get_object_or_404(Entertain, pk=pk)
    neweview.views += 1
    neweview.save()
    comments = Eomment.objects.filter(post=neweview)
    comment = int(Eomment.objects.filter(post=neweview).count())
    newes = Entertain.objects.all().exclude(pk=pk)
    neweis = random.sample(list(newes), min(len(list(newes)), 5))
    paginator = Paginator(neweis, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(int(comment))
    context = {
        "Entertain":neweview,
        "EntertainRelated":neweis,
        "page_obj":page_obj,
        "comments":comments,
        "commentcount":comment
    }
    return render(request, "Entertain/EntertainDetail.htm", context)
    
    
    
    
    
    
    
    






