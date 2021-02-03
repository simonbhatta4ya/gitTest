from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.generic import TemplateView, ListView
import random

# Create your views here.
"""
def home_view_old(request):
    num_ber = random.randint(0, 100000000)
    html_var = 'I am a context variable replaced by using python 3 > f strings'
    html_ = f'''<!DOCTYPE html><html lang=en><head></head><body><h6>hello wrld</h6><p>Main web HTMl string title</p><p>this is a {html_var}</p><p> This is a Random No : {num_ber}</body></html>'''
    #return HttpResponse('hello ....')
    return HttpResponse(html_)
    #return render(request, 'home.html', {'html_var': html_var})
    #return render(request, 'home.html', {'html_var': 'context variable'})
"""
"""
def home_view_new(request):
    html_var_ = 'django templates keys variable tempalte substitution..'
    num_ber = None
    some_list = [random.randint(0, 100000000),random.randint(0, 100000000),random.randint(0, 100000000)]
    condition_bool_item = True
    if condition_bool_item:
        num_ber = random.randint(0, 100000000)
    #return render(request, 'home.html', {'html_var': True})
    #return render(request, 'home.html', {'html_var' : html_var_ , 'num' : num_ber})
    context = {
        'bool_item' : True, 
        'num' : num_ber, 
        'some_list': some_list,
        'html_var': html_var_
        }
    return render(request, 'home.html', context)

"""

# This is Vol02 Seasn 01 episode 016 chapter - 006

"""
def home_view(request):
    num_ber = None
    some_list = [random.randint(0, 100000000),random.randint(0, 100000000),random.randint(0, 100000000)]
    condition_bool_item = True
    if condition_bool_item:
        num_ber = random.randint(0, 100000000)
    #return render(request, 'home.html', {'html_var': True})
    #return render(request, 'home.html', {'html_var' : html_var_ , 'num' : num_ber})
    context = {
        #'bool_item' : True, 
        'num' : num_ber, 
        'some_list': some_list
        }
    return render(request, 'home.html', context)

def about_view(request):
    context = {

    }
    return render(request, 'about.html', context)

def contact_view(request):
    context = {

    }
    return render(request, 'contact.html', context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        #print(kwargs)
        #print(request.POST.get('kwargs'))  # NOT WORKING
        context = {

        }
        return render(request, 'contact.html', context)



class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


"""


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        #print(context)
        num_ber = None
        some_list = [random.randint(0, 100000000),random.randint(0, 100000000),random.randint(0, 100000000)]
        condition_bool_item = True
        if condition_bool_item:
            num_ber = random.randint(0, 100000000)
        context = {
            'num' : num_ber,
            'some_list': some_list
        }
        return context

# class AboutView(TemplateView):
#     template_name = 'about.html'


# class ContactView(TemplateView):
#     template_name = 'contact.html'









