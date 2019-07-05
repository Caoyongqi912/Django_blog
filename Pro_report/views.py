from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Pro_Api.models import ApiTest
from Product.models import Product


class Report(View):
    def get(self,request,pid):
        return render(request,'apply/product/report/report.html',{'pid':pid})





class ApiReprot(View):
    def get(self, request):
        api_list = ApiTest.objects.all()
        api_count  = ApiTest.objects.all().count()
        print('api_count',api_count)
        api_pass_count = ApiTest.objects.filter(api_test_res=True).count()
        api_fail_count = api_count - api_pass_count
        data  = {
            'api_list':api_list,
            'api_count':api_count,
            'api_pass_count':api_pass_count,
            'api_fail_count':api_fail_count,
        }
        return render(request, 'apply/product/api/api_report.html', data)