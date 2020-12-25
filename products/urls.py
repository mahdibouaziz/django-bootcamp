from django.urls import path,include

from . import views

urlpatterns = [
    path('search/',views.search_view,name="search_view"),
    path('product/<int:pk>/',views.product_detail_view,name="product_view"),
    path('api/product/<int:pk>/',views.product_api_detail_view,name="product_api_view"),
    path("list_products/",views.products_list_view,name="products_list"),
    path("bad-view/",views.bad_view,name="bad_view"),
    path("product/create/",views.product_create_view,name="product_create"),
    path("get-name/",views.get_name,name="get_name"),

]
