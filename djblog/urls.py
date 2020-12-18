"""djblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from article import views #article klasöründeki views dosyasını import ettik
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = "index"), # '' içini boş bırakınca localhost:8000 yazınca bu url adresi çalışır. Çalışacak fonksiyonu ise article klasöründeki views.py'ye yazıyoruz.
    path('about/',views.about,name = "about"),
    path('articles/',include("article.urls")), #article kalıbını gördükten sonra git articledaki urls'e bak ve url'de arama işlemi gerçekleştir demek
    path('user/',include("user.urls")), #user/login user/logout tarzı url geldiği zaman bu çalışacak
]
#path('detail/<int:id>',views.detail,name = "detail") Dinamik url adresi yapımı

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)