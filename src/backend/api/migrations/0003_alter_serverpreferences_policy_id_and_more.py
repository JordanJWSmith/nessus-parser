# Generated by Django 4.0 on 2021-12-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_serverpreferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverpreferences',
            name='policy_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='serverpreferences',
            name='server_preferences_value',
            field=models.CharField(max_length=1000),
        ),
    ]
