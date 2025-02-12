from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse

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
    
class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV", "price":500}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":1000}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":100}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":20},
    ] 
 
class ProductIndexView(View): 
    template_name = 'products/index.html' 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
 
        return render(request, self.template_name, viewData) 
 
class ProductShowView(View): 
    template_name = 'products/show.html' 
    def get(self, request, id):  
        try:
            id = int(id)
            if id < 1 or id > len(Product.products):
                raise IndexError
            
            viewData = {} 
            product = Product.products[id - 1]
            viewData["title"] = product["name"] + " - Online Store" 
            viewData["price"] = product["price"]
            viewData["subtitle"] = product["name"] + " - Product information" 
            viewData["product"] = product
            
            return render(request, self.template_name, viewData)

        except (ValueError, IndexError):
            return HttpResponseRedirect(reverse("home"))