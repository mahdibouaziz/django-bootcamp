from django.http import HttpResponse,JsonResponse, Http404
from django.shortcuts import render

from .models import Product

# Create your views here.
def home_view(request):
    return HttpResponse("<h1>This is your home view</h1>")


# class HomeView():
#     pass



def product_detail_view(request,pk):
    try:
        product=Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404

    return HttpResponse(f"Product id: {product.id} Product Title: {product.title}")



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
