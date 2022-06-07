
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('post/',include('apps.viewtest.urls'),name='post'),
    path('myurl/',include('apps.urltest.urls'),name='myurl'),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
