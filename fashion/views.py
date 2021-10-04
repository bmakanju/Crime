from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from fashion.models import Fomment, Fashion,  ReadLaterFashion
import random
#

#Getting All Cment for post
def FashionCommentAll(request, pk):
    post = get_object_or_404(Fashion, pk=pk)
    comments = Fomment.objects.all().filter(post=post, is_approved=True)
    return JsonResponse({
        "comment":list(comments.values())
    })
    
    
    

#Comment For Fashion News
def FashionComment(request):
    print(request.user)
    posts = request.POST.get("post")
    messages = request.POST.get("content")
    userc = request.user
    postes = get_object_or_404(Fashion,pk=posts)
    commentsave = Fomment(names=request.user, content=messages, post=postes)
    commentsave.save()
    return redirect("fashion:fashionview" ,title=postes.title ,headline=postes.headline ,pk=postes.pk)
    
    
    
    
    
#ReadLaterFashion and also delete
def SaveFashion(request):
    pk = request.POST.get("value")
    news = get_object_or_404(Fashion, pk=pk)
    user_saving = request.user
    if ReadLaterFashion.objects.filter(news=news).exists():
        ReadLaterFashion.objects.get(news=news).delete()
        readlater = ReadLaterFashion.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("Fashion News  Newly added")
    else:
        readlater = ReadLaterFashion.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("Fashion News added")
    
    
#View All save for later 
def ReadLater(request):
    users = request.user
    read= ReadLaterFashion.objects.filter(name=users)
    context = {
        "read":read
    }
    return render(request, "Fashion/ReadLaterFashion.htm", context)
    


#View All Fashion
class Fashions(ListView):
    template_name = "Fashion/Fashion.htm"
    paginate_by = 25
    context_object_name = "Fashion"
    queryset = Fashion.objects.all()

#Viewing A particular Fashion
def FashionView(request, title, headline, pk):
    neweview = get_object_or_404(Fashion, pk=pk)
    neweview.views += 1
    neweview.save()
    comments = Fomment.objects.filter(post=neweview)
    comment = int(Fomment.objects.filter(post=neweview).count())
    newes = Fashion.objects.all().exclude(pk=pk)
    neweis = random.sample(list(newes), min(len(list(newes)), 5))
    paginator = Paginator(neweis, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(int(comment))
    context = {
        "Fashion":neweview,
        "FashionRelated":neweis,
        "page_obj":page_obj,
        "comments":comments,
        "commentcount":comment
    }
    return render(request, "Fashion/FashionDetail.htm", context)
    
    
    
    
    
    
    
    






