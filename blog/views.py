from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from blog.models import Comment,Blog, ReadLaterBlog
import random
#Editing Comment
def EditComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        content = request.POST.get("content")
        poie = request.POST.get("post")
        posts = get_object_or_404(Blog, pk=poie)
        comment.delete()
        commentsave = Comment(cmaster=request.user, post=posts, comments=content)
        commentsave.save()
        return redirect("blog:blogview", title=comment.post.btitle, headline=comment.post.descr , pk=comment.post.pk)
    else:
        context = {
            "comment":comment
        }
        return render(request, "Comment/EditComment.htm", context)
        
        
    
    


#Main Deleting Power Comment
def DeleteComment1(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect("blog:blogview", title=comment.post.btitle, headline=comment.post.descr , pk=comment.post.pk)

#Deleting Comment
def DeleteComment2(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    context = {
        "comment":comment
    }
    return render(request, "Comment/DeleteComment.htm", context)
#Getting All Cment for post
def BlogCommentAll(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.all().filter(post=post)
    return JsonResponse({
        "comment":list(comments.values())
    })
    
#Like system for Blog
def LikePost(request):
    pk = request.POST.get("pk")
    post = Blog.objects.get(pk=pk)
    user = request.user.id
    liked = False
    if post.likes.filter(id=user).exists():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True
        
    return JsonResponse({
        "liked":liked,
        "likecount":post.likes.count()
    })
    
#Heart system for Blog
def LovePost(request):
    pk = request.POST.get("pk")
    post = Blog.objects.get(pk=pk)
    user = request.user.id
    liked = False
    if post.heart.filter(id=user).exists():
        post.hate.remove(user)
        post.heart.remove(user)
        liked = False
    else:
        post.hate.remove(user)
        post.heart.add(user)
        liked = True
        
    return JsonResponse({
        "liked":liked,
        "heartcount":post.heart.count()
    })
    
    
 #Dislike system for Blog
def HatePost(request):
    pk = request.POST.get("pk")
    post = Blog.objects.get(pk=pk)
    user = request.user.id
    liked = False
    if post.hate.filter(id=user).exists():
        post.likes.remove(user)
        post.hate.remove(user)
        post.heart.remove(user)
        liked = False
    else:
        post.likes.remove(user)
        post.heart.remove(user)
        post.hate.add(user)
        liked = True
        
    return JsonResponse({
        "liked":liked,
        "hatecount":post.hate.count()
    })
    

#Comment For Blog Post
def BlogComment(request):
    print(request.user)
    posts = request.POST.get("post")
    messages = request.POST.get("bpost")
    userc = request.user
    postes = get_object_or_404(Blog,pk=posts)
    if messages == "":
        return HttpResponse("Comment Box can't be Null")
    else:
        commentsave = Comment(cmaster=request.user, comments=messages, post=postes)
        commentsave.save()
        return HttpResponse("Comment Saved ")
    #redirect("blog:blogview" ,title=postes.btitle ,headline=postes.descr ,pk=postes.pk)
  
    
    
    
    
#ReadLaterBlog and also delete
def SaveBlog(request):
    pk = request.POST.get("value")
    news = get_object_or_404(Blog, pk=pk)
    user_saving = request.user
    if ReadLaterBlog.objects.filter(name=request.user, news=news).exists():
        ReadLaterBlog.objects.get(news=news).delete()
        readlater = ReadLaterBlog.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("Blog Post Already Exists")
    else:
        readlater = ReadLaterBlog.objects.create(name=user_saving, news=news)
        readlater.save()
        return HttpResponse("Blog Post added")
    
    
#View All save for later 
def ReadLater(request):
    users = request.user
    read= ReadLaterBlog.objects.filter(name=users)
    context = {
        "read":read
    }
    return render(request, "Blog/ReadLaterBlog.htm", context)
    


#View All Blog
class Blogs(ListView):
    template_name = "Blog/Blog.htm"
    paginate_by = 25
    context_object_name = "Blog"
    queryset = Blog.objects.all()

#Viewing A particular Blog
def BlogView(request, title, headline, pk):
    neweview = get_object_or_404(Blog, pk=pk)
    neweview.views += 1
    neweview.save()
    comments = Comment.objects.filter(post=neweview)
    comment = int(Comment.objects.filter(post=neweview).count())
    newes = Blog.objects.all().exclude(pk=pk)[0:5]
    neweis = random.sample(list(newes), min(len(list(newes)), 5))
    paginator = Paginator(neweis, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(int(comment))
    context = {
        "Blog":neweview,
        "BlogRelated":neweis,
        "page_obj":page_obj,
        "comments":comments,
        "commentcount":comment
    }
    return render(request, "Blog/BlogDetail.htm", context)
    
    
    
    
    
    
    
    






