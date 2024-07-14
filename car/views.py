from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Car,Contact,Rent,Payment




# Create your views here. Python Functions
def inde(request):
    
    return render(request, 'inde.html')

def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username=request.POST['uname']
        email= request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                print('Email is already taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                print('Username is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User created')
                return redirect('login')
             
        else:
            mesaages.info(request, 'Password not matching')
            return render(request, 'register.html')
         
    
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            
            login(request, user)  # Renamed the login function to auth_login
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")
    

def logout(request):
    auth.logout(request)
    return redirect('login')

 
def home(request):
    return render(request, 'home.html')

def cars(request):
    
    car=Car.objects.all()
     
    params={'car':car}
    return render(request, 'cars.html',params)

def contact(request):
    if request.method=="POST":
        conname=request.POST['fullname']
        conemail=request.POST['email']
        conphone=request.POST['phone']
        conmessage=request.POST['message'] 
        contact = Contact(name = conname, email = conemail, phone_number = conphone,message = conmessage)
        contact.save()    
    
        
    return render(request, 'contact.html')

def rent(request,car_id): 
    car=Car.objects.get(pk=car_id)
    data={'car':car}
    # print("Car Name:", data['car'].car_name)
    # print("Price:", data['car'].price)
    # print("Seating Capacity:", data['car'].car_seater)
    # print("Fuel Type:", data['car'].car_fuel) 
    return render(request, 'rent.html' , data)

def Rent(request):
    if request.method=="POST":
        # uid=request.POST['user_id']
        name=request.POST['fullname']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        city=request.POST['city']
        car_name=request.POST['carname']
        car_seater=request.POST['carseat']
        car_fuel=request.POST['carfuel']
        price=request.POST['carprice']
        noofdays=request.POST['noofdays']
        fromdate=request.POST['fromdate']
        todate=request.POST['todate']
        loc_from=request.POST['floc']
        loc_to=request.POST['tloc']
        totalbill= request.POST['totalbill']
        order = Rent(name=name, email=email, phone=phone, address=address, city=city, car_name=car_name, car_seater=car_seater, price=price, car_fuel=car_fuel, days_for_rent=noofdays, fromdate=fromdate, todate=todate, loc_from=loc_from, loc_to=loc_to, totalbill=totalbill)
        order.save()
        return redirect('payment') 
    
    return render(request, 'rent.html')



def payment(request):
    if request.method=="POST":
        cardholdername=request.POST['cardname']
        cardnumber=request.POST['cardnumber']
        expdate=request.POST['expdate']
        cvv=request.POST['cvv']
        amo=Rent.objects.get('totalbill')
        data={'amo':amo}
        amount=request.POST['amount']
        payment = Payment(cardo=cardnumber,expdate=expdate,cvv=cvv,cardholder=cardholdername, amount=amount)
        payment.save()
        return redirect('payconf')
    
    
    return render(request, 'payment.html')

def about(request):
    return render(request, 'about.html')

def payconf(request):
    return render(request, 'payconf.html')

def profile(request):
    return render(request, 'profile.html')

def serve(request):
    return render(request, 'serve.html')




     