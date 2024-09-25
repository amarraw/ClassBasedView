from django.urls import path
from . import views


urlpatterns = [
    path("",views.AllCompany.as_view(), name="list"),
    path("<int:pk>", views.Companydetails.as_view(), name="detail"),
    # path("<int:pk>", views.Companydetails.as_view(), name="detail"),
    
    path("create/",views.Addcompany.as_view(),name="create"),    
    path("update/<int:pk>", views.UpadateCompany.as_view(), name="update"),
    path("updatecar/<int:pk>", views.UpdateCar.as_view(), name="updatecar"),
    path("addproduct", views.AddProduct.as_view(), name="addproduct"),
    path("delete/<int:pk>", views.DeleteCompany.as_view(), name="delete"),
    path("deletepro/<int:pk>", views.DeletePro.as_view(), name="deletepro")
    
]

