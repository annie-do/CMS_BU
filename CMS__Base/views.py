from django.shortcuts import render
## import HttpResponse
from django.http import HttpResponse

# Create your views here.

## from CMS > CMS_Base > templates > CMS > ...Template
def home(request):
    return render(request, 'CMS/main.html')

def about(request): 
    return render(request, 'CMS/aboutTemplate.html')

def contact(request):
    return render(request, 'CMS/contactTemplate.html')