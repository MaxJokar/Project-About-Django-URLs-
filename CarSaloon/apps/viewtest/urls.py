from django.urls import path
# import apps.formtest.views as views
from apps.viewtest.views import *


urlpatterns = [

    # path('index/',views.index,name="post_index"), #name helps  Reverse to get and give the url after get name 
    path('view0/',hello),
    path('view1/',ViewClass1.as_view(),name="viewClass1"),#Added    .as_view ()   when we access to a "generic class" as view 
    path('add/',PostCreate.as_view(),name="PostCreate"),
    path('list/',PostList.as_view(),name="PostList"),# we can use the name for  return reverse for the name!
    path('allist/',GenericClass1.as_view(),name="PostList2"),
    path('paginetest/',GenericClass3.as_view(),name="PostList3"),
    path('listpaginet/',fun1,name="PostList4"),
    path('list5/',GenericClass5.as_view(),name="PostList5"),
    path('detail/<int:pk>',PostDetail.as_view(),name="PostDetail"), #detail needs id(<int:pk>) we should add here by number. <int:pk> shows the details number!
    path('update/<int:pk>',PostUpdate.as_view(),name="PostUpdate"),
    path('delete/<int:pk>',PostDelete.as_view(),name="PostDelete"),
    
    
    
    
    
]