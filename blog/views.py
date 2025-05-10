from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage  # Assuming you have this model
from .models import Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product
from django.conf import settings
import paypalrestsdk
from django.shortcuts import render, redirect







def menu_view(request):
    
    return render(request, 'blog.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # Save to the database
        
        ContactMessage.objects.create(name=name, email=email, message=message)
        return HttpResponse("Thank you for your message!")
    return render(request, 'contact.html')



def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query) if query else Product.objects.all()
    return render(request, 'store/search.html', {'products': products, 'query': query})


  # Ensure Product model is imported






def about(request):
    return render(request, 'blog/about.html')




#login

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
    return render(request, 'blog/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)  # Auto-login after registration
        return redirect('dashboard')
    return render(request, 'blog/register.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    return render(request, 'blog/dashboard.html')
def home(request):
    return render(request, 'blog/home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


 

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_SECRET
})

def create_payment(request):
    if request.method == "POST":
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "transactions": [{
                "amount": {"total": "19.99", "currency": "USD"},
                "description": "Purchase from FStore"
            }],
            "redirect_urls": {
                "return_url": request.build_absolute_uri("/payment-success"),
                "cancel_url": request.build_absolute_uri("/payment-cancel")
            }
        })

        if payment.create():
            return redirect(payment.links[1].href)  # Redirect user to PayPal checkout
        else:
            return render(request, "payment.html", {"error": "Payment failed"})
    
    return render(request, "payment.html")

# Create your views here.
