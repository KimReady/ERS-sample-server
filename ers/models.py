from django.db import models


class ErrorLog(models.Model):
    reg_date = models.DateTimeField()
    log_date = models.DateTimeField()
    android_id = models.CharField(max_length=50)
    package_name = models.CharField(max_length=100)
    app_version = models.CharField(max_length=30)
    sdk_version = models.IntegerField()
    phone_brand = models.CharField(max_length=50)
    phone_model = models.CharField(max_length=50)
    log_level = models.CharField(max_length=30)
    tag = models.CharField(max_length=50)
    message = models.TextField()
    stacktrace = models.TextField()
    available_memory = models.IntegerField()
    total_memory = models.IntegerField()
    custom_data = models.TextField()

