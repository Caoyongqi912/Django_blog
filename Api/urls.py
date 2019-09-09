from django.urls import path

from Api.views import Api_test

app_name='Api'
urlpatterns = [
    path('api/',Api_test.as_view(),name='api')
]