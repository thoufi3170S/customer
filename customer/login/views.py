from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
# def login(request):
#    return render(request,'crm/login.html')
# def loginentered(request):
#   if request.method == "POST":
#     username = request.POST['username']
#     password = request.POST['password']
#     print("*************pass entered*********************")
#     print(username)
#     print(password)
    
#     user = auth.authenticate(username=username,password=password)
#     if user is not None:
#       auth.login(request, user)
#       print("************************user verified************************************")
#       return redirect('customer_list')
#     else:
#       print("******************user missmatched ******************************")
#       messages.info(request,'invalid credentiial')
#       return redirect('login1')
#   else:
#     return render(request,'crm/login.html')
def contact(request):
    return render(request,'crm/contact.html')
def logout(request):
  auth.logout(request)
  return redirect('/')

  
 