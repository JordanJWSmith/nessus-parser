# Generated by Django 4.0 on 2021-12-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_individualpluginselection'),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
    ]