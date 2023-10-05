# Generated by Django 4.2.6 on 2023-10-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=50)),
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
