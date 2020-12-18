from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
# Oluşturulan modeller admin.py de kayıt edilmeli
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE) #on_delete yazar silinirse makaleyide sil demek
    #Eğer sitede author yazısını türkçeleştirmek istersek () içine verbose_name = "Yazar" şeklinde yazmamız lazım.
    title = models.CharField(max_length=50)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True) #biz zaman vermiyoruz veri eklendiği anki zamanı kendisi oto verir
    article_image = models.FileField(blank = True,null= True,verbose_name="Add image to article") #doluda olabilir boşta olabilir.
    def __str__(self):
        return self.title #normalde admin panelinde article yazınca article object(1) şeklinde gözüküyordu. bu kod ile title ile gözükecek adı. Title yerine author filanda yazılabilir.

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name="Article",related_name="comments")
    comment_author = models.CharField(max_length=500,verbose_name="Name")
    comment_content = models.CharField(max_length=500,verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
    
      




