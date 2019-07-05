from django.contrib import admin

# Register your models here.
from Pro_Api.models import ApiTestStep, ApiTest


@admin.register(ApiTestStep)
class ApiTestStepAdmin(admin.ModelAdmin):
    list_display = ('api_name', 'api_url', 'api_step', 'api_param_val', 'api_method', 'api_result', 'api_response',
                    'api_status', 'create_time', 'api_test')


@admin.register(ApiTest)
class ApiTestAdmin(admin.ModelAdmin):
    list_display = ('api_test_name', 'api_test_desc', 'api_tester', 'api_test_res', 'create_time', 'product')

