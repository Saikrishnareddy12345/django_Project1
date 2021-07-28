from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def run(request):
    a="<h2><b>Offers of the Day buy one get one Vivo mobile in Flipkart</b></h2>"
    return HttpResponse(a)
