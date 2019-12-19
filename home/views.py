from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View

def home(request):

    a = 10
    b = 20
    c = a * b

    return render(request, 'home.html', {'result': c})


def my_logout(request):
    logout(request)
    return redirect('home')

class HomePageView(TemplateView):
    template_name = 'home2.html'

class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home3.html')