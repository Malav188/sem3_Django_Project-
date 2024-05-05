# Generated by Django 5.0 on 2023-12-16 08:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cosutomer_detailes',
            fields=[
                ('username', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('meter_num', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(max_length=150, null=True)),
                ('email', models.EmailField(default='', max_length=254, null=True)),
                ('mobile_num', models.CharField(max_length=10, null=True)),
                ('pan', models.CharField(max_length=10, null=True)),
                ('gst', models.CharField(max_length=15, null=True)),
                ('ty', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='employee_detailes',
            fields=[
                ('employeee_id', models.CharField(max_length=12, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(max_length=150, null=True)),
                ('email', models.EmailField(default='', max_length=254, null=True)),
                ('mobile_num', models.CharField(max_length=10, null=True)),
                ('qualification', models.CharField(max_length=20)),
                ('data_added', models.BooleanField(default=False)),
                ('user', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='reading',
            fields=[
                ('bill_number', models.AutoField(primary_key=True, serialize=False)),
                ('r_date', models.DateField(default='dd-mm-yyyy')),
                ('reading', models.FloatField()),
                ('price', models.FloatField(default=True)),
                ('total', models.FloatField(blank=True, editable=False, null=True)),
                ('user', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bill.cosutomer_detailes')),
            ],
        ),
        migrations.CreateModel(
            name='pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ty_pay', models.CharField(max_length=20, null=True)),
                ('data_add', models.BooleanField(default=False)),
                ('user', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bill_number', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to='bill.reading')),
            ],
        ),
    ]