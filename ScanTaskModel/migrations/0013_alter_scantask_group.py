# Generated by Django 3.2.1 on 2021-07-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScanTaskModel', '0012_scantask_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scantask',
            name='group',
            field=models.CharField(default='1', max_length=100),
        ),
    ]