# Generated by Django 3.0.2 on 2020-03-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0003_auto_20200319_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobenquiry',
            name='At',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
