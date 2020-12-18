from django.contrib import admin
from django.urls import path
from . import views #şu anki klasörün üzerindeki views'ı alma işlemi
app_name = "article" #yön belirtmek için(şu dosyanın içindeki şu dosya tarzı) name belirlemek önemli

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"), 
    path('addarticle/',views.addArticle,name = "addarticle"), 
    path('article/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateArticle,name = "update"),
    path('delete/<int:id>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"), #article sayfası için burası. '' içini boş bıraktık zaten blog kısmındaki urls'te dahil etmiştik onu.
    path('comment/<int:id>',views.addComment,name = "comment"),
]












