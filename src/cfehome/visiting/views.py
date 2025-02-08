from django.shortcuts import render
from .models import Page_visits

# Create your views here.


def aboutview(request):
  return visit(request)
 

def visit(request):
  qs=Page_visits.objects.all()
  count=Page_visits.objects.count()
  my_context={
    "name":"dammu",
    
    "count":qs.count()
  }
  print('path' ,request.path)
  Page_visits.objects.create()
  return  render(request,"home.html",my_context)

