# Generated by Django 3.2.1 on 2021-07-14 03:27

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
                ('taskid', models.IntegerField(default=1)),
                ('ip', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]