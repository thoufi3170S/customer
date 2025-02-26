from django.urls import path
from .import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    # path('',views.login,name="loginentry"),
    # path('loginentered/',views.loginentered,name="loginentered"),
    path('logout/',views.logout,name="logout"),
    path('contact/',views.contact,name="contact"),
    # path('register',views.register,name="register"),
    # path('home',views.frst,name="home")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
