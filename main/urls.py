from django.urls import path
from . import views

urlpatterns=[
  path('add/',views.add_num,name='add_numbers'),
  path('pnr/',views.simple_interest,name='simple_interest'),
  ]