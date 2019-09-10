from django.urls import path

from Api.views import Api_test, Api_send

app_name = 'Api'
urlpatterns = [
    path('requests/', Api_test.as_view(), name='requests'),
    path('send/', Api_send.as_view(), name='send')
]
