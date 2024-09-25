from django.contrib import admin
from django.urls import path , include
from cbvapp.views import Myclass 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("company/", include("cbvapp.urls")),
    path("", Myclass.as_view(), name="index" ),
    path("admin/", admin.site.urls),
]   +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)