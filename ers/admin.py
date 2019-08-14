from django.contrib import admin
from .models import ErrorLog


class ReportAdmin(admin.ModelAdmin):
    list_display = ['reg_date', 'package_name', 'app_version', 'sdk_version', 'phone_brand', 'phone_model', 'log_level', 'tag', 'message']
    list_display_links = ['reg_date', 'package_name', 'app_version', 'sdk_version', 'phone_brand', 'phone_model', 'log_level', 'tag', 'message']
    list_filter = ['sdk_version', 'phone_brand', 'phone_model', 'log_level', 'tag', 'message']
    search_fields = ['package_name', 'app_version', 'phone_brand', 'phone_model', 'tag', 'message']


admin.site.register(ErrorLog, ReportAdmin)
