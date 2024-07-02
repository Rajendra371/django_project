from django.urls import path
from .views import admin_home
from .import views


urlpatterns = [
    path('dashboard/',admin_home),
    path('product/',views.product,name='Product'),
    path('customer/',views.customer,name='Customer')


]
