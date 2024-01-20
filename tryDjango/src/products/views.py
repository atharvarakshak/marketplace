from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import Http404
from .models import Product
from .forms import ProductForm,RawProductForm
# Create your views here.


# def render_initial_data(request):
#     initial_data={
#         'title':"A django page   ",

#     }
#     obj=Product.objects.get(id=14)
#     form=ProductForm(request.POST or None,instance=obj)
#     if form.is_valid():
#          form.save()
        
#     context={ 
#         "form":form
#     }
    
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)


# dynamic url
# def dynamic_lookup_view(request,my_id):
#     # obj = Product.objects.get(id=my_id)
#     # obj = get_object_or_404(Product,id=my_id)
#     try:
#         obj = Product.objects.get(id=my_id)
#     except Product.DoesNotExist:
#         raise Http404
    
#     context={
#         'object':obj
#     }
#     return render(request, "products/product_detail.html",context)


def product_detail_view(request):
    obj = get_object_or_404(Product, id=id)
    
    context={
        'object':obj
    }
    return render(request, "products/product_detail.html",context)

def product_delete_view(request,id):
    obj=get_object_or_404(Product,id=id)
    if request.method=="POST":
        # confirming  delete
        obj.delete()
        return redirect('../../')
    context={
        "object":obj
    }

    return render(request,"products/product_delete.html",context)

# def product_delete_view(request,my_id):
#     queryset=Product.objects.all()
#     context={
#         "object":obj
#     }

#     return render(request,"products/product_delete.html",context)



def product_list_view(request):
    queryset=Product.objects.all()
    context={
        "object_list":queryset
    }

    return render(request,"products/product_list.html",context)

     
def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None )
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)