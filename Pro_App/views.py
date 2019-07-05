from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Pro_App.models import AppCase
from Product.models import Product


class AppCaseView(View):
    def get(self, request, pid):
        product = Product.objects.get(pk=pid)
        appcase = AppCase.objects.filter(product=product)
        return render(request, 'apply/product/app/appcase.html', {'appcase': appcase})
