# Generated by Django 4.2.5 on 2023-09-04 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=20)),
                ('account_name', models.CharField(max_length=200)),
                ('created_by', models.CharField(default='Auto', max_length=30)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default='Auto', max_length=30)),
                ('void', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=1)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_id', models.CharField(max_length=20)),
                ('account_from', models.CharField(max_length=20)),
                ('account_to', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('remark', models.CharField(max_length=200)),
                ('created_by', models.CharField(default='Auto', max_length=30)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default='Auto', max_length=30)),
                ('void', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=1)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
    ]
