from django.http import HttpResponse, JsonResponse
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
        log = parse_log(request_body)
        log.save()
    return JsonResponse({})


@csrf_exempt
def register_error_logs(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        for body in request_body:
            log = parse_log(body)
            log.save()
    return JsonResponse({})


def parse_log(request_body):
    return ErrorLog(
        reg_date=request_body['reg_date'],
        android_id=request_body['android_id'],
        package_name=request_body['package_name'],
        app_version=request_body['app_version'],
        sdk_version=request_body['sdk_version'],
        phone_brand=request_body['phone_brand'],
        phone_model=request_body['phone_model'],
        log_level=request_body['log_level'],
        message=request_body['message'],
        stacktrace=request_body['stacktrace'],
        available_memory=request_body['available_memory'],
        total_memory=request_body['total_memory'],
        company=request_body['company'],
        name=request_body['name'],
        email=request_body['email']
    )