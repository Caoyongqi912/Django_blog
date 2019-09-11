from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from common.RequestPool import RequestPool


class Api_test(View):
    def get(self, request):
        return render(request, 'apply/Api/Api.html')


class Api_send(View):
    def post(self, request):
        url = request.POST.get('url', '')
        method = request.POST.get("method", '')
        res = RequestPool().requestTool(method=method, url=url)
        data = {
            'status': 'ok',
            'res': res.text
        }
        return JsonResponse(data)


