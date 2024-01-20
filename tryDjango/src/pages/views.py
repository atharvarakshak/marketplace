from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# create web pages here
# urls and routing , django templates,

def home_view(request,*args,**kwargs):  
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1 >hello world</h1>")
    return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
      return render(request,"contact.html",{})

def about_view(request,*args,**kwargs):
    my_context={
         "my_text":"this is about sec",
         "my_number": 12345,
         "ok":True,
         "my_list":[12,21,34,34,55,"Abc"],
         "html_text":"<h1>hello world</h1>"
    }
 
    return render(request,"about.html",my_context)

def social_view(request,*args,**kwargs):
    return HttpResponse("<h1> social Page </h1>")
