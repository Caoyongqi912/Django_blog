import json

import requests
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


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


class RequestPool:
    def __init__(self):
        self.res = None

    def requestTool(self, method, url, headers=None):
        if method == 'GET':
            try:
                self.res = requests.get(url=url, headers=headers)
            except Exception as e:
                print(e)
                return False
        else:
            try:
                self.res = requests.post(url=url, headers=headers)
            except Exception as e:
                print(e)
                return False

        return self.res
