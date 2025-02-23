from django.contrib import admin
from django.urls import path, include
from .views import CustomerViewSet ,customer_list,LeadViewSet,TaskViewSet,ReportViewSet,lead,projects,reports,task,sales,contact,login,loginentered,search,CRMEventViewSet,calendar_view,send_crm_email,events_api
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'events', CRMEventViewSet)
router.register(r'customers', CustomerViewSet),
router.register(r'leads', LeadViewSet),
router.register(r'tasks', TaskViewSet)
router.register(r'report', ReportViewSet)

urlpatterns = [
    
    path('',login,name='login'),
    # path('admin/', admin.site.urls),
    path('loginentered/',loginentered,name="loginentered"),
    path('search/', search, name='search'),
    path('customer_list', customer_list, name='customer_list'),
    path('task/', task, name='task'),
    path('lead/', lead, name='lead'),
    path('projects/', projects, name='projects'),
    path('sales/', sales, name='sales'),
    path('reports/', reports, name='reports'),
    path('contact/', contact, name='contact'),
    path('calendar/', calendar_view, name='calendar_view'),
    path('compose-email/', send_crm_email, name='compose_email'),
    path('api/events/', events_api, name='events_api'),
    path('api/', include(router.urls)) 



]
