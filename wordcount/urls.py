from wordcount import views
from django.urls import path
from . import views

urlpatterns = [   
     path('',views.homepage,name='home'),
     path('contact/',views.contact),
     #path('count/',views.count),
     path('counts/',views.count, name='count'),
     
     #Assignment
     path('about',views.about,name='about'),
     
]
