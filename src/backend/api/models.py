from django.db import models

# Create your models here.
class policy(models.Model):
    file_hash = models.CharField(max_length=32)
    policy_name = models.CharField(max_length=1000)
    policy_comments = models.CharField(max_length = 1000)


class serverPreferences(models.Model):
    policy_id = models.IntegerField()
    server_preferences_name = models.CharField(max_length=1000)
    server_preferences_value = models.CharField(max_length=1000000)


class pluginPreferences(models.Model):
    policy_id = models.PositiveIntegerField()
    pluginName = models.CharField(max_length=1000)
    pluginId = models.PositiveIntegerField()
    fullName = models.CharField(max_length=1000)
    preferenceName = models.CharField(max_length=1000)
    preferenceType = models.CharField(max_length=1000)
    preferenceValues = models.CharField(max_length=1000)
    selectedValue = models.CharField(max_length=1000)


class familySelection(models.Model):
    policy_id = models.PositiveIntegerField()
    FamilyName = models.CharField(max_length=1000)
    Status = models.CharField(max_length=1000)


class individualPluginSelection(models.Model):
    policy_id = models.PositiveIntegerField()
    PluginId = models.PositiveIntegerField()
    PluginName = models.CharField(max_length=1000)
    Family = models.CharField(max_length=1000)
    Status = models.CharField(max_length=1000)


class report(models.Model):
    policy_id = models.PositiveIntegerField()
    name = models.CharField(max_length=1000)


class reportHost(models.Model):
    policy_id = models.PositiveIntegerField()
    name = models.CharField(max_length=1000)


class hostProperties(models.Model):
    report_host_id = models.PositiveIntegerField()
    tag_name = models.CharField(max_length=1000)
    tag_value = models.CharField(max_length=1000)


class reportItem(models.Model):
    report_host_id = models.PositiveIntegerField()
    port = models.CharField(max_length=100) 
    svc_name = models.CharField(max_length=1000)
    protocol = models.CharField(max_length=1000)
    severity = models.CharField(max_length=1000)
    pluginID = models.PositiveIntegerField()
    pluginName = models.CharField(max_length=1000)
    pluginFamily = models.CharField(max_length=1000)


class reportItemProperties(models.Model):
    report_item_id = models.PositiveIntegerField()
    property_name = models.CharField(max_length=1000)
    property_value = models.CharField(max_length=1000000)

