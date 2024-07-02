from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userspage.uth import admin_only

# Create your views here.
@login_required
@admin_only

def admin_home(request):
    return render(request, 'admins/dashboard.html')



def product(request):
    return render(request, 'admins/product.html')


def customer(request):
    return render(request,'admins/customer.html')
