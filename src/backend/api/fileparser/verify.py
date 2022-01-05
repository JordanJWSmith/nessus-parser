from ..serializers import policySerializer, serverPreferencesSerializer, pluginPreferencesSerializer, familySelectionSerializer, individualPluginSelectionSerializer, reportSerializer, reportHostSerializer, hostPropertiesSerializer, reportItemSerializer, reportItemPropertiesSerializer
import logging


def policy_verify(obj, file_hash):
    details = {
        'file_hash': file_hash,
        'policy_name': obj[0],
        'policy_comments': obj[1]
    }
    serializer = policySerializer(data=details)
    return serializer.is_valid()


def server_preferences_verify(obj, id):
    for preference in obj:
            details = {
                'policy_id': id,
                'server_preferences_name': preference['name'],
                'server_preferences_value': preference['value']
            }
            serializer = serverPreferencesSerializer(data=details)
            if not serializer.is_valid():
                logging.info('server_preferences ' + str(serializer.is_valid()))
                logging.info('details: ' + str(details))
                return False
    return True


def plugin_preferences_verify(obj, id):
    for preference in obj:
        preference['policy_id'] = id
        if not preference.get('selectedValue'):
            preference['selectedValue'] = 'None'
        serializer = pluginPreferencesSerializer(data=preference)
        if not serializer.is_valid():
            logging.info('plugin_preferences ' + str(serializer.is_valid()))
            logging.info('details: ' + str(preference))
            logging.info('fields: ' + str(serializer.get_fields()))
            return False
    return True


def server_and_plugins_verify(obj, id):
    server_preferences = obj['ServerPreferences']
    plugin_preferences = obj['PluginsPreferences']
    return server_preferences_verify(server_preferences, id) and plugin_preferences_verify(plugin_preferences, id)


def family_selection_items_verify(obj, id):
    for item in obj:
        item['policy_id'] = id
        serializer = familySelectionSerializer(data=item)
        if not serializer.is_valid():
            logging.info('family_selection ' + str(serializer.is_valid()))
            logging.info('details: ' + str(item))
            return False
    return True


def individual_plugin_items_verify(obj, id):
    for item in obj:
        item['policy_id'] = id
        serializer = individualPluginSelectionSerializer(data=item)
        if not serializer.is_valid():
            logging.info('individual_plugin_items ' + str(serializer.is_valid()))
            logging.info('details: ' + str(item))
            return False
    return True


def report_name_verify(name, id):
    details = {
            'policy_id': id,
            'name': name
        }
    serializer = reportSerializer(data=details)
    return serializer.is_valid()


def report_host_verify(name, id):
    details = {
            'policy_id': id,
            'name': name
        }
    serializer = reportHostSerializer(data=details)
    return serializer.is_valid()


def host_properties_verify(obj, report_host_id):
    for tag, value in obj.items():
        details = {
            'report_host_id': report_host_id,
            'tag_name': tag,
            'tag_value': value
        }
        serializer = hostPropertiesSerializer(data=details)
        if not serializer.is_valid():
            logging.info('host_properties ' + str(serializer.is_valid()))
            logging.info('details: ' + str(details))
            return False
    return True


def report_item_verify(obj, report_host_id):
    obj['report_host_id'] = report_host_id
    serializer = reportItemSerializer(data=obj)
    return serializer.is_valid()


def report_item_properties_verify(obj, report_item_id):
    for property_name, property_value in obj.items():
        details = {
            'report_item_id': report_item_id,
            'property_name': property_name,
            'property_value': property_value
        }
        serializer = reportItemPropertiesSerializer(data=details)
        if not serializer.is_valid():
            logging.info('report_item_properties ' + str(serializer.is_valid()))
            logging.info('details: ' + str(details))
            return False
    return True


def report_section_verify(obj, id):
    for name, details in obj.items():
        host_props, rep_items = details['host_properties'], details['report_items']
        if report_host_verify(name, id) and host_properties_verify(host_props, id):
            for item in rep_items:
                if not report_item_verify(item['item_attrib'], id) or not report_item_properties_verify(item['item_values'], id):
                    return False
        else:
            return False
    return True
        

def verify_data(parsed_file, hash):
    return policy_verify(parsed_file['policy'], hash) and \
        server_and_plugins_verify(parsed_file['server_and_plugins'], 1) and \
        family_selection_items_verify(parsed_file['family_selection_items'], 1) and \
        individual_plugin_items_verify(parsed_file['individual_plugin_selection_items'], 1) and \
        report_name_verify(parsed_file['report_name'], 1) and \
        report_section_verify(parsed_file['report_hosts'], 1)