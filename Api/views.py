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
        res = RequestPool().requestTool(method, url)
        if res:
            res = json.dumps(json.loads(res.text), indent=4)
            data = {
                'status': 'ok',
                'res': res
            }
            return JsonResponse(data)
        else:
            data = {
                'status': 'err'
            }
            return JsonResponse(data)


class RequestPool:
    def __init__(self):
        self.res = None

    def requestTool(self, method, url, headers=None):

        if method == 'GET':
            try:
                self.res = requests.get(url=url, headers=headers)
            except Exception:
                return False
        elif method == "POST":
            try:
                self.res = requests.post(url=url, headers=headers)
            except Exception as e:
                return False
        elif method == "PUT":
            try:
                self.res = requests.put(url=url, headers=headers)
            except Exception as e:
                return False
        else:
            try:
                self.res = requests.delete(url=url, headers=headers)
            except Exception as e:
                return False

        return self.res
