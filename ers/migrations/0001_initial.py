# Generated by Django 2.2.4 on 2019-08-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField()),
                ('android_id', models.CharField(max_length=50)),
                ('package_name', models.CharField(max_length=100)),
                ('app_version', models.CharField(max_length=30)),
                ('sdk_version', models.IntegerField()),
                ('phone_brand', models.CharField(max_length=50)),
                ('phone_model', models.CharField(max_length=50)),
                ('log_level', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('stacktrace', models.TextField()),
                ('available_memory', models.IntegerField()),
                ('total_memory', models.IntegerField()),
                ('company', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
