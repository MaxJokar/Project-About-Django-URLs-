from django.urls import path, re_path
from apps.urltest.views import *
import re
# from django.conf.urls import include, url #env\lib\site-packages\django\conf\urls\__init__.py)






urlpatterns = [
    path('u1/',viewfun1,name='u1'),
    path(r'u2/<str:name>/<int:age>/',viewfun6, name='u2'), #http://127.0.0.1:8000/myurl/u2/max/42/
    # re_path(r'^u5/(?P<name>[a-z]{5})/$', viewfun5, name='u5'), # +  means at least one char:{5} must be only 5 char:can be between 35={3,5}
    re_path(r'^u6/(?P<name>[a-z]{3,5})/(?P<age>[0-9]+)/$',viewfun6,name='u6'),
    re_path(r'^u7/(?P<name>[a-z]{3,5})/(?:age-(?P<age>\d+)/)?$',viewfun6,name='u7'), #:age- means :age should be in URL 
    re_path(r'^u8/hello/(?P<name>[a-z]{3,5})/(?:age-(?P<age>\d+)/)?$',viewfun6,name='u8'),#http://127.0.0.1:8000/myurl/u8/hello/max/age-400/
    re_path(r'^u9/укр/(?P<name>[a-z]{3,5})/(?:age-(?P<age>\d+)/)?$',viewfun6,name='u9'),# other letters also work :http://127.0.0.1:8000/myurl/u9/%D1%83%D0%BA%D1%80/max/age-400/
    re_path(r'^u10/укр/(?P<name>[-\w])/(?:age-(?P<age>\d+)/)?$',viewfun6,name='u10'),#if you have a another alphabets [-\w] helps us avoi ERROR ;
    #  [-\w]:- must be used if we have - among our names  like  :ed-ger: myurl/u9/hello-people/max/age-42
    re_path(r'^/укр/(?P<name>[-\w])/(?:age-(?P<age>\d+)/)?$',viewfun6,name='u10'), #without having  u11 :myurl/hello-people/max/age-42
    re_path(r'^v/(?P<name>[-\w])/(?:age-(?P<age>\d+)/)?$',viewfun6,name='u10'),#To avoid mistake about  languges from right to left put one character first v/
    #/v/салам
     
    
    # path(r'^u3/',viewfun1,name='u3'),
    path('u10/',viewfun10 ,name='u10'), #http://127.0.0.1:8000/myurl/u10/?name=max&age=44
    
    path('u11/',viewfun11 ,name='u11'),
    
]








