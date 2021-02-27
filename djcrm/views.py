from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home_page.html"


def home_page(request):
    return render(request, 'home_page.html')
