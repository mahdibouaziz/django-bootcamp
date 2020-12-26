from django.http import HttpResponse,JsonResponse, Http404
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from .models import Product


from .forms import NameForm

# Create your views here.

# def get_name(request):
#     #we check the request is POST or not
#     if request.method =="POST":

#         #we create an instance and give it the data from the request
#         form=NameForm(request.POST)

#         #check it's valid
#         if form.is_valid():
#             #we can get the data now

#             #don't forget we have a "cleaned_data" attribute
#             name=form.cleaned_data.get("your_name")

#             #do what you want with the name ....
#             #we use get in the dictionary because if the attribute doesn't exist it will just escape it
#             return redirect ("where you want to go")
#     else:
#         form=NameForm()
#     context={
#         "form":form,
#     }
#     return render(request,"name_form.html",context)

#Method2 
def get_name(request):
    
    #we create an instance and give it the data from the request or None (in case we don't have a POST request)
    form=NameForm(request.POST or None)

    #check if it's valid (if we don't have a POST request it will return false)
    if form.is_valid():
        #we can get the data now

        #don't forget we have a "cleaned_data" attribute
        name= form.cleaned_data.get("your_name")
        print(f"Your name is {name}")
        #do what you want with the name ....
        #we use get in the dictionary because if the attribute doesn't exist it will just escape it
        return redirect ("get_name")

    context={
        "form":form,
    }

    return render(request,"name_form.html",context)


#Don't do this type of GET handeling, it works but it's not secure
def bad_view(request):
    my_request_data=dict(request.GET)
    print(my_request_data)
    
    Product.objects.create(title=my_request_data.get('title')[0],content=my_request_data.get('content')[0], price=my_request_data.get("price")[0])
    return HttpResponse("Don't do this")

#This is a good view
def search_view(request):
    query=request.GET.get('q')
    qs= Product.objects.filter(title__icontains=query[0])
    print(qs)
    context={
        "name":"Mahdi"
    }
    return render(request,template_name="home.html",context=context)

#The best way to handle the POST request in Django is the Built in way using django forms because it's more secure
# def product_create_view(request):

#     # print(request.POST)
#     # print(request.GET)
    
#     if request.method=="POST":
#         post_data=request.POST or None

#         if post_data:
#             my_form=ProductForm(request.POST)
            
#             if my_form.is_valid():
#                 print(my_form.cleaned_data.get("title"))
#                 # print(post_data)
#                 title_from_input=my_form.cleaned_data.get("title")
#                 Product.objects.create(title=title_from_input)
#                 return redirect("product_create")

#     context={}
#     return render(request,template_name="products/forms.html",context=context)

@login_required
def product_create_view(request):

    form=ProductForm(request.POST or None)

    if form.is_valid():
        
        obj=form.save(commit=False)
        #Do some stuff with the cleaned object before saving to the DB
        #by default commit=True if you put it it will directly save it to the database
        obj.user=request.user
        obj.save()


        # print(form.cleaned_data)
        # data=form.cleaned_data
        
        #This is a way to send a kwarg args : a dictionary with key-value pairs
        # Product.objects.create(**data) # or you can use the first option
        return redirect("product_create")

    context={
        "form":form,
    }
    return render(request,template_name="products/forms.html",context=context)




def product_detail_view(request,pk):
    try:
        product=Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404

    context={
        "product":product,
    }

    return render(request,"products/detail.html",context)

def products_list_view (request):
    try:
        products=Product.objects.all()
    except:
        raise Http404

    context={
        "products":products,
    }

    return render(request,"products/list.html",context)


def product_api_detail_view(request,pk):
    try:
        product=Product.objects.get(id=pk)
    except:
        return JsonResponse({"message":"Not found"})

    return JsonResponse({
        "id":product.id,
        "title":product.title,
        "content":product.content,
    })
