# Generated by Django 4.2.3 on 2024-04-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_studentmodel_alter_moviemodel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
