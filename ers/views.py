from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from ers.models import ErrorLog
import json

def index(request):
    return HttpResponse("Welcome to ERS!")

def get_current_time(request):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return JsonResponse({
        'currentTime': now,
    })

@csrf_exempt
def register_error_log(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        log = ErrorLog(
            reg_date=request_body['reg_date'],
            android_id=request_body['android_id'],
            package_name=request_body['package_name'],
            sdk_version=request_body['sdk_version'],
            phone_brand=request_body['phone_brand'],
            phone_model=request_body['phone_model'],
            log_level=request_body['log_level'],
            message=request_body['message'],
            stacktrace=request_body['stacktrace'],
            available_memory=request_body['available_memory'],
            total_memory=request_body['total_memory'])
        log.save()
    return JsonResponse({})
