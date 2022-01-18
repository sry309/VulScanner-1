# Generated by Django 3.2.1 on 2021-06-10 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('port', models.IntegerField(default=0)),
                ('isActive', models.BooleanField(default=False)),
                ('speciality', models.CharField(default='', max_length=100)),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
    ]