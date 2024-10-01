from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='homepage'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('products/<str:name>/',views.Products,name='products'),
    path('products/<str:category_name>/<str:product_name>/', views.purchase, name='purchase'),
    path('category/<str:name>/', views.Products, name='products'),
    path('category/',views.category,name='category'),
    path('aboutcontact/',views.about,name='about'),
    path('create-payment/', views.create_payment, name='create_payment'),
    path('paypal-return/', views.paypal_return, name='paypal_return'),
    path('paypal-cancel/', views.paypal_cancel, name='paypal_cancel'),
]