from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# def messageview(request):
#     return render(request,'home.html')

class Messageview(TemplateView):
    template_name = 'home.html'