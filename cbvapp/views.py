from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View , TemplateView , ListView , DeleteView , DetailView , CreateView , UpdateView
# Create your views here.
from .models import Company , Car
from django.urls import reverse_lazy

class Myclass(TemplateView):
    template_name="index.html"

class AllCompany(ListView):
    model = Company
    template_name = "company_list.html"
    context_object_name = "allcompanies"  # Ensure this matches in the template

class Companydetails(DetailView):
    model = Company
    context_object_name = "company_details"

class Addcompany(CreateView):
    model = Company
    fields = "__all__"
    template_name = "cbvapp/company_form.html"
    # success_url = reverse_lazy("company_list")
    
    # def form_valid(self, form):
    #     return super().form_valid(form)

class UpadateCompany(UpdateView):
    model = Company
    fields = ["name", "ceo"]

class UpdateCar(UpdateView):
    model = Car
    fields = ["car_name", "fuel_type","seat_capicity","is_rooftoop","cars_img"]

    success_url = reverse_lazy("list")
    
class AddProduct(CreateView):
    model = Car
    fields = "__all__"

    success_url = reverse_lazy("list")
    

class DeleteCompany(DeleteView):
    model = Company
    success_url = reverse_lazy("list")

class DeletePro(DeleteView):
    model = Car 
    success_url = reverse_lazy("list")
