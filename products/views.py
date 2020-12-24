from django.http import HttpResponse,JsonResponse, Http404
from django.shortcuts import render

from .models import Product

# Create your views here.

def home_view(request):
    context={
        "name":"Mahdi"
    }
    return render(request,template_name="home.html",context=context)


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
        "content":product.content
    })
