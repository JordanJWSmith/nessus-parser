# Generated by Django 4.0 on 2021-12-26 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_rename_family_individualpluginselection_family_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familyselection',
            old_name='family_name',
            new_name='FamilyName',
        ),
        migrations.RenameField(
            model_name='familyselection',
            old_name='status',
            new_name='Status',
        ),
    ]
