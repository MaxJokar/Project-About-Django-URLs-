from django.shortcuts import render

def viewfun1(request):
    context={
        'name':'Maxxx',
        'age':42
    }
    return render(request,'urltest/page1.html',context)




#http://127.0.0.1:8000/myurl/u2/David/23/
def viewfun2(request,name,age):
    context={
        'name':name,
        'age':age
        # 'family':family
    }
    return render(request,'urltest/page1.html',context)




def viewfun5(request,name): #http://127.0.0.1:8000/myurl/u2/max/42/
    context={
        'name':name,
        'age':42
   
    
    }
    return render(request,'urltest/page1.html',context)





def viewfun6(request,name,age): #http://127.0.0.1:8000/myurl/u2/max/42/   :http://127.0.0.1:8000/myurl/u7/maxim/age-400/
    context={
        'name':name,
        'age':age
    
    }
    return render(request,'urltest/page1.html',context)


#If  our Function doenst  have any  "internal Parameters like: /u7/max/age-42 " ,but wants to get "QueryString " from URL like myurl/u10?
#? in url means QueryString :Example: myurl/u10?name=max&age=42&family=jokar>PAY ATTENTION these ones are not our internam Parameters but we can access 
#our functin by: request.GET.get!



def viewfun10(request): 
    name=request.GET.get('name')
    age=request.GET.get('age')
    
    context={
        'name':name,
        'age':age
    
    }
    return render(request,'urltest/page1.html',context)





#check safe url,reverse, urlencode:
#reverse('u8')=>To get Address of URL in our view!It Gets your a string
from django.urls import reverse  #reverse: To change name of  a  URL to Address of that URL :
from urllib.parse import urlencode  # To Make a   QueryString in URL  OR  change a  dictionary to a  QueryString
# from django.utils.http import is_safe_url 
#Verifies security of a specific  URL ,gives Boolean:we Obliged what sites are Allowed 
 
def viewfun11(request):
    # if not is_safe_url(url="urltest/u1", allowed_hosts={'mysite.com'}, requre_https=True):
    #if not is_safe_url(url="urltest/u1", allowed_hosts=request.get_host()):=>means Only Internal URLs
        # return render(request,'urltest/error.html')
    base_url=reverse('u10')
    print(base_url)
    query_string=urlencode({'name':'Max','age':100})  # IT will be converted  in  :?name=max&age=100   inURL 
    print(query_string)
    #Format String:{}{}
    url=f'{base_url}?{query_string}' # if we (http://127.0.0.1:8000/myurl/u11/) in terminal we can see:/myurl/u10/?name=Max&age=100
    # url='{}?{}'.format(base_url,query_string)
    print(url) #Prints in Terminal:/myurl/u10/?name=Max&age=100
    age=request.GET.get('age') #in URL we type:http://127.0.0.1:8000/myurl/u11/?age=90 Then we will see  the age on form
    context={'age':age}
    return render(request,'urltest/page1.html',context)

















