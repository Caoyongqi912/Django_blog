from django.contrib import admin

# Register your models here.
from Pro_App.models import AppCase, AppCaseStep


@admin.register(AppCase)
class AppCaseAdmin(admin.ModelAdmin):
    list_display =  ('app_case_name','app_case_result','app_tester','create_time')

@admin.register(AppCaseStep)
class AppCaseStepAdmin(admin.ModelAdmin):
    list_display = ('app_test_step','app_sbj_name','app_find_method','app_element','app_opt_method',
                    'app_test_data','app_assert_data','app_res','create_time')
