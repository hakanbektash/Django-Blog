from django.contrib import admin

from .models import Article,Comment  # .models şuanki klasörden models kısmını ifade eder.

# Register your models here.
admin.site.register(Comment)
#Bizim uygulama oluşturduğumuzu djangoya söylememiz lazım o yüzden djblog'daki settingstede kayıt etmemiz lazım.

@admin.register(Article) #decoraterler bazen class'lardada kullanılır onun bir örneği;
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"] #articles kısmında title author date bilgileride gözükür böylece.
    #list_display_links = ["author"] # bu özellik link ekler. Böylece title ile authora da basıldığında linke gider.
    #Searchbox ekleme
    search_fields = ["title"] # title bilgisine göre arama yapılabilir böylece.
    #Hangi ayda günde makale oluşturulmuş bilgisini gösterme;
    list_filter = ["created_date"]
    class Meta:
        model = Article          