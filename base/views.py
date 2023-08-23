from django.shortcuts import render,HttpResponse
from .models import Category,Doctors

# Create your views here.
def home(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'base/index/index.html',context)

def doctorList(request,pk):
    category=Category.objects.get(id=pk)
    doclist=Doctors.objects.filter(category=category)
    context={'category':category,'doclist':doclist}
    return render(request,'base/Doctorlist/doctorList.html',context)

def docDetails(request):
    return render(request,'base/Doctordetails/doc.html')
