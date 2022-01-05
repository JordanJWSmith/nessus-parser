from rest_framework import serializers
from .models import policy, serverPreferences, pluginPreferences, familySelection, individualPluginSelection, report, reportHost, hostProperties, reportItem, reportItemProperties


class FieldMixin(object):
    def get_field_names(self, *args, **kwargs):
        field_names = self.context.get('fields', None)
        if field_names:
            return field_names

        return super(FieldMixin, self).get_field_names(*args, **kwargs)


class policySerializer(FieldMixin, serializers.ModelSerializer):
    file_hash = serializers.CharField(max_length=32)
    policy_name = serializers.CharField(max_length=1000)
    policy_comments = serializers.CharField(max_length=None)

    class Meta:
        model = policy
        fields = ('__all__')


class serverPreferencesSerializer(serializers.ModelSerializer):
    policy_id = serializers.IntegerField()
    server_preferences_name = serializers.CharField(max_length=1000)
    server_preferences_value = serializers.CharField(max_length=1000000, trim_whitespace=False)

    class Meta:
        model = serverPreferences
        fields = ('__all__')


class pluginPreferencesSerializer(serializers.ModelSerializer):
    policy_id = serializers.IntegerField()
    pluginName = serializers.CharField(max_length=1000)
    pluginId = serializers.IntegerField()
    fullName = serializers.CharField(max_length=1000)
    preferenceName = serializers.CharField(max_length=1000)
    preferenceType = serializers.CharField(max_length=1000)
    preferenceValues = serializers.CharField(max_length=1000)
    selectedValue = serializers.CharField(max_length=1000)

    class Meta:
        model = pluginPreferences
        fields = ('__all__')


class familySelectionSerializer(serializers.ModelSerializer):
    policy_id = serializers.IntegerField()
    FamilyName = serializers.CharField(max_length=1000)
    Status = serializers.CharField(max_length=1000)

    class Meta:
        model = familySelection
        fields = ('__all__')


class individualPluginSelectionSerializer(serializers.ModelSerializer):
    policy_id = serializers.IntegerField()
    PluginId = serializers.IntegerField()
    PluginName = serializers.CharField(max_length=1000)
    Family = serializers.CharField(max_length=1000)
    Status = serializers.CharField(max_length=1000)

    class Meta:
        model = individualPluginSelection
        fields = ('__all__')


class reportSerializer(serializers.ModelSerializer):
    policy_id = serializers.IntegerField()
    name = serializers.CharField(max_length=1000)

    class Meta:
        model = report
        fields = ('__all__')



class reportHostSerializer(serializers.ModelSerializer):
    policy_id = serializers.IntegerField()
    name = serializers.CharField(max_length=1000)

    class Meta:
        model = reportHost
        fields = ('__all__')



class hostPropertiesSerializer(serializers.ModelSerializer):
    report_host_id = serializers.IntegerField()
    tag_name = serializers.CharField(max_length=1000)
    tag_value = serializers.CharField(max_length=1000)

    class Meta:
        model = hostProperties
        fields = ('__all__')


class reportItemSerializer(serializers.ModelSerializer):
    report_host_id = serializers.IntegerField()
    port = serializers.CharField(max_length=100)
    svc_name = serializers.CharField(max_length=1000)
    protocol = serializers.CharField(max_length=1000)
    severity = serializers.CharField(max_length=1000)
    pluginID = serializers.IntegerField()
    pluginName = serializers.CharField(max_length=1000)
    pluginFamily = serializers.CharField(max_length=1000)

    class Meta:
        model = reportItem
        fields = ('__all__')


class reportItemPropertiesSerializer(serializers.ModelSerializer):
    report_item_id = serializers.IntegerField()
    property_name = serializers.CharField(max_length=1000)
    property_value = serializers.CharField(max_length=1000000, trim_whitespace=False)

    class Meta:
        model = reportItemProperties
        fields = ('__all__')



