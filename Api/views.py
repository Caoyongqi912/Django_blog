from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from common.RequestPool import RequestPool
from common.Ua import UserAgentPool


class Api_test(View):
    def get(self, request):
        return render(request, 'apply/Api/Api.html')


class Api_send(View):
    def post(self, request):
        url = request.POST.get('url', '')
        method = request.POST.get("method", '')
        if url and method:
            res = RequestPool().requestTool(method=method.strip(), url=url.strip(), headers=UserAgentPool().ua())
            data = {
                'status': 'ok',
                'res': res.text,
                'code': res.status_code
            }
            return JsonResponse(data)
        else:
            data = {
                'res': 'fail'
            }
            return JsonResponse(data)
