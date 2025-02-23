from django.shortcuts import render,redirect,HttpResponse
from .models import Customer,Lead
from rest_framework import viewsets
from .models import Customer,Lead,Task,Sale,Contact,Report,CRMEvent,Event
from .serializers import CustomerSerializer,LeadSerializer,TaskSerializer,ReportSerializer,CRMEventSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CRMEmail
import json

def login(request):
      print("thoufi")
      return render(request,'crm/login.html')
def loginentered(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    print("*************pass entered*********************")
    print(username)
    print(password)
    
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request, user)
      print("************************user verified************************************")
      return redirect('customer_list')
    else:
      print("******************user missmatched ******************************")
      messages.info(request,'invalid credentiial')
      return redirect('login')
  else:
    return render(request,'crm/login.html')

def customer_list(request):
    customers = Customer.objects.all()
    tasks=Task.objects.all()
    sales=Sale.objects.all()
    leads= Lead.objects.all()
    contacts=Contact.objects.all()
    reports=Report.objects.all()
    calendar=CRMEvent.objects.all()
    section_name = request.GET.get('section_name', None)
    print(section_name)
    return render(request,'crm/demo.html',{'customers':customers,'tasks':tasks,'section_name':section_name,'sales':sales,'leads':leads,'contacts':contacts,'reports':reports,'calendar':calendar})
def task(request):
    tasks=Task.objects.all()
    sales=Sale.objects.all()
    section_name = request.GET.get('section_name', None)
    print(section_name)
    return render(request,'crm/demo.html',{'tasks':tasks,'section-name':section_name,'sales':sales})

def lead(request):
     leads= Lead.objects.all()
     return render(request,'crm/leads.html',{'leads':leads})
def sales(request):
    sales=Sale.objects.all()
    return render(request,'crm/sales.html',{'sales':sales})

def projects(request):
    return render(request,'crm/projects.html')

def contact(request):
    contacts=Contact.objects.all()
    return render(request,'crm/contact.html',{'contacts':contacts})


def reports(request):
     reports=Report.objects.all()
     return render(request,'crm/Reports.html',{'reports':reports})
def search(request):
    if request.method == "POST":
        section_name = request.POST.get('section_name', None)
        print("true block")
        username = request.POST['username']
        data11 = Customer.objects.all()
        print(username)
        print(section_name)
        # section_name="search"
        if section_name =='search' :
            print("inner loop")
            data = data11.filter(name=username)
            return render(request,'crm/demo.html',{"section_name":section_name,"data":data})
             
    else:
       customer=Customer.objects.all()
       return render(request,'crm/home.html',{'customer':Customer})
    
def calendar_view(request):
    return render(request, 'crm/calendar.html')

def send_crm_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        recipient = request.POST.get('recipient')
        message = request.POST.get('message')

        try:
            send_mail(subject, message, 'your_email@gmail.com', [recipient])
            CRMEmail.objects.create(subject=subject, recipient=recipient, message=message, status='Sent')
            return JsonResponse({'status': 'success', 'message': 'Email Sent Successfully'})
        except BadHeaderError:
            CRMEmail.objects.create(subject=subject, recipient=recipient, message=message, status='Failed')
            return JsonResponse({'status': 'error', 'message': 'Invalid Header Found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})

    

def events_api(request):
    if request.method == 'GET':
        events = list(Event.objects.values())
        print("firtst check----")
        print(events)
        return JsonResponse(events, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        event = Event.objects.create(
            title=data['title'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            reminder=data.get('reminder', False),
            reminder_time=data.get('reminder_time')
        )
        print("second check---- ",event)
        return JsonResponse({'status': 'success', 'id': event.id})

    elif request.method == 'DELETE':
        event_id = request.GET.get('id')
        Event.objects.filter(id=event_id).delete()
        return JsonResponse({'status': 'deleted'})

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
class CRMEventViewSet(viewsets.ModelViewSet):
    queryset = CRMEvent.objects.all()
    serializer_class = CRMEventSerializer



