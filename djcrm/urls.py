from django.contrib import admin
from django.urls import path, include
from .views import home_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads"))
]
