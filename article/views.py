from django.shortcuts import (render,HttpResponse,redirect,get_object_or_404,reverse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from django.core.mail import EmailMessage
from django.template.loader import get_template

from .forms import ArticleForm,ContactForm
from .models import Article,Comment


# Create your views here.

tem_dir ="articles/"

def articles(request):
    query = request.GET.get("keyword")
    articles = Article.objects.all()
    
    if query:
        articles = Article.objects.filter(
            Q(title__icontains = query)|
             Q(content__icontains = query)
             ).distinct()
        # render(request,tem_dir+"articles.html",context)

    paginator = Paginator(articles,10)
    
    # page_request_var="page"
    page = request.GET.get('page',1) 
    
    # ?page = 2 
    articles = paginator.get_page(page)
    
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)



    context ={
            "articles":articles,
            "object_list":queryset,
            # "page_request_var":page_request_var,

                }

    return render(request,tem_dir+"articles.html",context)



def index(request):
    return render(request,tem_dir+"index.html")
    
def about(request):
    return render(request,tem_dir+"about.html")


@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Article Created successfully")
        return redirect("article:dashboard")
    return render(request,tem_dir+"addarticle.html",{"form":form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()   
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()
    return render(request,tem_dir+"detail.html",{"article":article,"comments":comments})



@login_required(login_url = "user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Article updated successfully")
        return redirect("article:dashboard")


    return render(request,tem_dir+"update.html",{"form":form})

@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)

    article.delete()

    messages.success(request,"Article deleted successfully")

    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))
    

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template =get_template(tem_dir+'contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submit from HarfhoBlog ",
                content,
                "Harfho Blog" +'',
                ['harfho77@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, tem_dir+'contact.html', {'form': form_class,})


