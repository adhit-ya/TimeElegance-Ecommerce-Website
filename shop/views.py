from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *
from urllib.parse import unquote


def Home(request):

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    
    return render(request,'index.html',{'username':username})

def about(request):
    return render(request,'aboutcontact.html')

def purchase(request,category_name,product_name):

    category_name = unquote(category_name) #it decode the encode categoryname and productname which was received from the web it encoded the url because to handle spave and special characters
    product_name = unquote(product_name)

    category = get_object_or_404(Category, name=category_name)

    # Fetch the product that belongs to this category and matches the product name
    product = get_object_or_404(Product, category=category, name=product_name)

    return render(request, 'purchase.html', {'product': product})

def Products(request, name):
    category = get_object_or_404(Category, name=name, status=0)
    products = Product.objects.filter(category=category)

    return render(request, 'products.html', {'products': products, 'category': category})

def category(request):
    categories = Category.objects.filter(status=0)
    return render(request, 'category.html', {'categories': categories}) 

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username,email,password)
                user.save()
                login(request,user)
                return redirect('/')
            except:
                error_message = "Error in creating account"
                return render(request,'signup.html',{'error_message':error_message})
        else:
            error_message = 'Password does not match'
            return render(request,'signup.html',{'error_message':error_message})
    return render(request,'signup.html')

def user_login(request):
    
    if request.method == 'POST':
        entered_username = request.POST['username']
        entered_password = request.POST['password']

        user = authenticate(request, username=entered_username, password=entered_password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')
