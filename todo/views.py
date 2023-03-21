from django.shortcuts import render,redirect

# Create your views here.

def todoList(request):
    if not request.session.get('id'):
        return redirect('login')
    
    return render(request,'todo-list.html')