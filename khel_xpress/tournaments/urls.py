# tournaments/urls.py
from django.urls import path
from . import views

urlpatterns = [
      path('organize/', views.register_tournament, name='organize'),
   

]
