# Generated by Django 4.0 on 2021-12-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_hostproperties'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_host_id', models.PositiveIntegerField()),
                ('port', models.CharField(max_length=100)),
                ('svc_name', models.CharField(max_length=1000)),
                ('protocol', models.CharField(max_length=1000)),
                ('severity', models.CharField(max_length=1000)),
                ('plugin_id', models.PositiveIntegerField()),
                ('plugin_name', models.CharField(max_length=1000)),
                ('plugin_family', models.CharField(max_length=1000)),
            ],
        ),
    ]
