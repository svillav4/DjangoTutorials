from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView): 
    template_name = 'pages/home.html'

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Samuel Villa", 
        }) 
        return context 
    
class ContactPageView(TemplateView): 
    template_name = 'pages/contact.html' 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({
            "title": "Contact information (Fake)",
            "email": "example@example.com", 
            "address": "Calle 51 # 81z - 99", 
            "phoneNumber": "+57 3174535678", 
        }) 
        return context 