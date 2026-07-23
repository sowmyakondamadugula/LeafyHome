from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login,logout
from .models import plant,user_numbers,cart_items
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.urls import reverse

# for Home page

products=plant.objects.order_by('?')[:8]
new_plants=plant.objects.order_by('?')[:8]

# for Shop page
deco=plant.objects.filter(category__name= "Decorative")
flowers=plant.objects.filter(category__name="Flowering plant")
veggies=plant.objects.filter(category__name="Vegetable plant")
others=plant.objects.filter(category__name="other plant")

def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password")
    return render(request, "login.html")


def signup(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        phone=request.POST.get("phone")

        try:
            validate_password(password)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return render(request, "signup.html")

        user=User.objects.create(
            username=username,
            password=password,
            email=email,
        )
        user_numbers.objects.create(
            user=user,
            phone=phone
        )
        return redirect('login')
    
    return render(request,"signup.html")


def home(request):
    return render(request,"home.html",{
        'active_page': 'home',
        'products': products,
        'new_plants': new_plants
    })
   
def shop(request):
    return render(request,"shop.html",{
        'active_page': 'shop',
        'deco': deco,
        'flowers':flowers,
        'veggies':veggies,
        'others':others
    })
 
def about(request):
    return render(request,"about.html",{
        'active_page': 'about'
    })

def contact(request):
    return render(request,"contact.html",{
        'active_page': 'contact'
    })

def cart(request):
    if request.user.is_authenticated:
        my_cart=cart_items.objects.filter(user=request.user)
        total=0
        for item in my_cart:
            item.subtotal= item.product.price * item.quantity
            total+=item.subtotal
        return render(request,"cart.html",{
            'active_page' : 'cart',
            'cart_items':my_cart,
            "total": total
        })
    else:
        return render(request,"cart.html")



def add_to_cart(request, id):
    
    if not request.user.is_authenticated:
        return JsonResponse({
            "login_required": True,
            "message": "Please log in to add items to your cart."
        }, status=401)

    product = plant.objects.get(id=id)

    cart_item = cart_items.objects.filter(
        user=request.user,
        product=product
    ).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_items.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )

    return JsonResponse({
            "message": "Product added to cart."
        })

def increase_quantity(request, id):
    cart_item = get_object_or_404(cart_items, id=id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("cart")

def decrease_quantity(request, id):
    cart_item = get_object_or_404(cart_items, id=id, user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect("cart")

def remove_from_cart(request, id):
    item = get_object_or_404(cart_items, id=id, user=request.user)
    item.delete()
    return redirect("cart")

def logout_user(request):
    logout(request)
    return redirect("home")