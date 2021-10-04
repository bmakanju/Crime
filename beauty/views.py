from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from beauty.models import Bomment, Beauty,ReadLaterBeauty
import random

#Getting All Cment for post
def BeautyCommentAll(request, pk):
    post = get_object_or_404(Beauty, pk=pk)
    comments = Bomment.objects.all().filter(post=post, is_approved=True)
    return JsonResponse({
        "comment":list(comments.values())
    })
    
    
    

#Comment For Beauty News
def BeautyComment(request):
    print(request.user)
    posts = request.POST.get("post")
    messages = request.POST.get("content")
    userc = request.user
    postes = get_object_or_404(Beauty,pk=posts)
    commentsave = Bomment(names=request.user, content=messages, post=postes)
    commentsave.save()
    return redirect("beauty:beautyview" ,title=postes.title ,headline=postes.headline ,pk=postes.pk)
    
    
    
    
    
#ReadLaterBeauty and also delete
def SaveBeauty(request):
    pk = request.POST.get("value")
    news = get_object_or_404(Beauty, pk=pk)
    user_saving = request.user
    if ReadLaterBeauty.objects.filter(news=news).exists():
        ReadLaterBeauty.objects.get(news=news).delete()
        readlater = ReadLaterBeauty.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("Beauty News  Newly added")
    else:
        readlater = ReadLaterBeauty.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("Beauty News added")
    
    
#View All save for later 
def ReadLater(request):
    users = request.user
    read= ReadLaterBeauty.objects.filter(name=users)
    context = {
        "read":read
    }
    return render(request, "Beauty/ReadLaterBeauty.htm", context)
    


#View All Beauty
class Beautys(ListView):
    template_name = "Beauty/Beauty.htm"
    paginate_by = 25
    context_object_name = "Beauty"
    queryset = Beauty.objects.all()

#Viewing A particular Beauty
def BeautyView(request, title, headline, pk):
    neweview = get_object_or_404(Beauty, pk=pk)
    neweview.views += 1
    neweview.save()
    comments = Bomment.objects.filter(post=neweview)
    comment = int(Bomment.objects.filter(post=neweview).count())
    newes = Beauty.objects.all().exclude(pk=pk)
    neweis = random.sample(list(newes), min(len(list(newes)), 5))
    paginator = Paginator(neweis, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(int(comment))
    context = {
        "Beauty":neweview,
        "BeautyRelated":neweis,
        "page_obj":page_obj,
        "comments":comments,
        "commentcount":comment
    }
    return render(request, "Beauty/BeautyDetail.htm", context)
    
    
    
    
    
    
    
    






