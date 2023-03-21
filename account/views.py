from django.shortcuts import render
from django.contrib import messages

# get and post login view
def login(request):
     return render(request,'login.html')

def register(request):
    
    if request.method == 'POST':
        error_message=""
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if not name:
            data = dict()
            messages.success(request, "Error: Name field is required.")
            return render(request,'register.html',data)
        elif not email:
            data = dict()
            messages.success(request, "Error: Email field is required.")
            return render(request,'register.html',data)
        elif not password:
            data = dict()
            messages.success(request, "Error: Password field is required.")
            return render(request,'register.html',data)
        else:
            return render(request,'register.html')
            
    else:
        return render(request,'register.html')

