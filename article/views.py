from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")
    if (keyword):
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all() #bu metod tüm articelları alacak ve bir tane listeye atacak.
    return render(request,"articles.html",{"articles":articles})
def index(request): #bu requestin her views dosyasında bulunması ve en başta olması gerekiyor.
    return render(request,"index.html") # template ile request gönderme işlemi
#    return HttpResponse("Anasayfa") # Http ile response  döndürüldü.
def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user) # sadece giriş yapmış kullanıcıların makalelerini almak için 'filter' metodunu kullandık
    context = {
        "articles" : articles
    }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False) # article ekleme formunu model haline getiridiğimiz için bu kadar kolay bir biçimde kaydedebiliriz veritabanına
        #commit = False ile commit işlemini yani save işlemini gerçekleştirme ben bunu özel olarak kendim gerçekleştireceğim demek.     
        article.author = request.user
        article.save() # commit işlemini burada kendimiz yapıyoruz. commit = False demesek hata veriyor böylece hatayı engelliyoruz.
        messages.success(request,"Article succesfully created")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})
def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id) #varsa değeri yoksa 404 sayfasını döndürecek
    comments = article.comments.all() #article'ın ilişkili olduğu comment'lerin hepisini alıyoruz.
    return render(request,"detail.html",{"article":article,"comments":comments})
@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article succesfully updated")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Article succesfully deleted")
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
    # articles/detail/15 şeklinde bir dinamik url yapısı tanımlanmış oldu.
