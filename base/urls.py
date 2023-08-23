from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctorlist/<int:pk>/',views.doctorList,name='doclist'),
    path('doctordetails/',views.docDetails,name='docDetails')
]
