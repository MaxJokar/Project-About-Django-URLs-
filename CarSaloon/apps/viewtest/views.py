from multiprocessing import context
from django.shortcuts import render
from django.views import View
from pyexpat import model

def hello(request):
    
        context={
            'name':'Hello Max Jokar & Django:This message is  from View Side: def hello(request):'
            
        }
        return render(request,'viewtest/page0.html',context)

#===================Season 5 ======================Views================================================================
class ViewClass1(View):
    def get(self,request):
        context={
            'name':'Max Jokar comes from ViewClass1'
            
        }
        return render(request, 'viewtest/page1.html',context)
#====================GENERIC CLASS====================== MODEl POST=====================================================
# Add your app in your setting , make model Post here, makemigrations, migrate Next STEP below:
#with the help of class  Generic of Django want to control create and work with views 
#we would like to write a class which can work on a specific Model:
# Class Base Generic Views: [Detail, Create,Edit ,Delete]operation :

from django.views.generic.edit import CreateView
from .models import Post
from django.urls import reverse 
#1.to create :
# instead def and etc by writing 2 lines  code we can handle everything here:/post/list/":post_list.html 
class PostCreate(CreateView):
    model=Post
    fields="__all__" #Till here all datas we Post are saved in our db but to observe them of our Page we need this:
    # 1.success_url="/post/list/"      # Displays what you Posted on your Form   :
    #or 2: 
    def get_success_url(self):
        return reverse('PostList') #name="PostList"
# After we run & see the form is ready to Observe:   http://127.0.0.1:8000/post/add/


#2.If a class follows the Generic ListView , It brings all datas as a listS  
from django.views.generic.list  import ListView
class PostList(ListView): #page2.html :As Default listView puts its list inside place or context named: object_list(in html)
        model=Post
# to handle The error Appears after we Post ,we should use:(def get_success_url)SuccessURL! above mentioned!

#==============Detail:========================================================================================
#To show details of a model we send  a foreign Key and by that fk we control it exist or not BUt here:

from django.views.generic.detail import DetailView
class PostDetail(DetailView):
    model=Post

#===========Update:===========================================================================================
from django.views.generic.edit import UpdateView

class PostUpdate(UpdateView):   #This function Displays the data recoded on  Form
    model=Post
    fields="__all__"
    success_url="/post/list/"
#============Delete===========================================================================================
from django.views.generic.edit import DeleteView


class PostDelete(DeleteView):  
    model=Post  #to create its html we use:name of our model:Post_Confirm_delete
    fields="__all__"
    success_url="/post/list/"
#in URL :http://127.0.0.1:8000/post/delete/2 YOu'll see a form asking to delete the page 2 or not ,submit?



#=======Change our Template Name:===============================post_list.html===========allist==================
class GenericClass1(ListView):
    model=Post
    template_name='viewtest/page2.html' #this line goes to post_list.html and opens it 
    # we can change The name of context which wants to convey the data to templates this way:
    #post_list.html  => Not {% for post in object_list %}  But {% for post in posts%} !
    context_object_name='posts' #Our datas dont go to Object_list , This way  goe to  post :
    #if we want to see in list  Only True or Only False and not all mixed we do the following:
    queryset=Post.objects.order_by('is_active') #we change the active like False the first one and not mixed in list 
    #to Display more Datas we use the following: Ex:posts+....
    #to main context which contains our posts add contextes mentioned name,family,...
    def get_context_data(self, **kwargs): # To add any datas to our context use this 
        context = super().get_context_data(**kwargs) #self :the main context,kwargs: our datas 
        context["name"] ="Max" 
        context["age"] ="54" 
        context["family"] ="Jokar" 
        return context
     

#===========PagiNet================================================================================================
#! in your db:SELECT title,description,is_active FROM  carsaloonseason5views.viewtest_post;
#insert into carsaloonseason5views.viewtest_post(title,description,is_active)
# SELECT title,description,is_active FROM  carsaloonseason5views.viewtest_post; several times execute it 

#To add PageNate:
class GenericClass3(ListView):
    model=Post
    template_name='viewtest/page3.html'
    context_object_name='posts'
    queryset=Post.objects.order_by('is_active')
    paginate_by=6   #1.instead of showing all records just every 6 records are Displayed:
    #2.pager added in our page3.html downloaded from :https://getbootstrap.com/docs/4.0/components/pagination/


#==============Paginate on  Funcation Class======================================================================
from django.core.paginator import Paginator

def fun1(request):
    posts=Post.objects.order_by('is_active')
    paginator=Paginator(posts, 10)
    page_number=request.GET.get('page') #Displays page Numberin URL if there is any query string named page read its value and put in page_number
    page_object=paginator.get_page(page_number)
    context={
        'page_obj':page_object
    }
    return render(request,'viewtest/page4.html',context)


#==========Dynamic Queryset def get_queryset ===================================================================

class GenericClass5(ListView):
    model=Post
    template_name='viewtest/page5.html'
    context_object_name='posts'
    queryset=Post.objects.order_by('is_active')
    paginate_by=6 
    
    # def get_queryset(self): #queryset=Post.objects.order_by('is_active')
    #     return super().get_queryset().filter(is_active=True).order_by('title')
    #Filtering in URL:
    
    def get_queryset(self): #queryset=Post.objects.order_by('is_active')
        title1=self.request.GET.get('title') #from URL read it put in title
        return Post.objects.filter(title=title1)
        # new_context=Post.objects.filter(title=title1)
        # return new_context
    #in URL write :http://127.0.0.1:8000/post/list5/?lastminute and see the result
    #OR check this way in URL:http://127.0.0.1:8000/post/list5/?title=test2








