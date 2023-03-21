from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from .models import Customer
# get and post login view
def login(request):
     if request.session.get('id'):
        return redirect('todo_list')
     
     if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            customer=Customer.objects.get(email=email) 
            if  customer:
               if check_password(password,customer.password):
                    data=dict()
                    messages.success(request,"Login successfully")
                    request.session['id']=customer.id
                    return redirect('todo_list')
               else:
                    messages.error(request,"Invalid email and password")
                    return redirect('login')
            else:
                messages.error(request,"Invalid email and password")
                return redirect('login')
        except Customer.DoesNotExist:
            customer=None               
            messages.error(request,"Invalid email and password")
            return redirect('login')                 
     else:
        return render(request,'login.html')

def register(request):
    if request.session.get('id'):
        return redirect('todo_list')
    if request.method == 'POST':
        error_message=""
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        new_password=make_password(password)
        customer=Customer(name=name,email=email,password=new_password)
        # please add this line i forget this line
        if customer.save() != True:
            data=dict()
            messages.success(request,"Registration Successfully")
            return redirect('login')
        else:
            data=dict()
            messages.error(request,"Registration not successfully")
            return redirect('register')
    else:
        return render(request,'register.html')


