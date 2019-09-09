from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class Api_test(View):
    def get(self, request):
        return render(request, 'apply/Api/Api.html')
