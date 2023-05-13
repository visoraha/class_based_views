from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
from app.forms import *
# Create your views here.

# functoin based view returning string
def fbv_string(request):
    return HttpResponse(' it is fbv_string')


# class based viwe returning string

class cbv_string(View):
    def get(self,request):
        return HttpResponse('it is class based view')
    
# function based view  returning html page
def fbv_html(request):
    return render(request,'fbv_html.html')



# class based view  returning html page
class cbv_html(View):
    def get(self,request):
            return render(request,'cbv_html.html')

# function based forms

def fbf_form(request):
     FBO=studentform()
     d={'FBO':FBO}
     if request.method=='POST':
          fd=studentform(request.POST)
          if fd.is_valid():
               fd.save()
               return HttpResponse('data is inserted')          
     return render(request,'fbf_form.html',d)
class cbf_form(View):
     def get(self, request):
        CBO=studentform()
        d={'CBO':CBO}
        return render(request,'cbf_form.html',d)
     def post(self, request):
        TFD=studentform(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')







