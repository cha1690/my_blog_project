# Generated by Django 3.0.2 on 2020-03-03 05:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200206_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
