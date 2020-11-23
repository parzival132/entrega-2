
from django.urls import path, include
from scooterlineapp import views 
from django.contrib.auth import login
from django.conf.urls import url

urlpatterns = [
    path('',views.inicio,name="inicio"),

    path('producto',views.producto,name="producto"),

    path('nosotros',views.nosotros,name="nosotros"),

    path('', include('django.contrib.auth.urls')),

    path('registrar_usuario',views.registrar_usuario,name="registrar_usuario"),

    path('redireccion',views.redireccion,name="redireccion"),
    
]
