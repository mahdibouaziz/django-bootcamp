from django.urls import path,include

from . import views

urlpatterns = [
    path('search/',views.home_view,name="home_view"),
    path('product/<int:pk>/',views.product_detail_view,name="product_view"),
    path('api/product/<int:pk>/',views.product_api_detail_view,name="product_api_view"),

]
