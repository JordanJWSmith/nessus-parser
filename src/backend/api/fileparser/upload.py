import requests, logging


def policy_upload(obj, file_hash):
    details = {
        'file_hash': file_hash,
        'policy_name': obj[0],
        'policy_comments': obj[1]
    }
    headers = {'Content-type': 'application/json'}
    res = requests.post(
        'http://localhost:8000/policy/', 
        json=details, 
        headers=headers)

    return {'res': res, 'id': res.json()['data']['id']}


def server_preferences_upload(obj, id):
    try:
        resdict = {}
        for preference in obj:
            details = {
                'policy_id': id,
                'server_preferences_name': preference['name'],
                'server_preferences_value': preference['value']
            }
            headers = {'Content-type': 'application/json'}
            res = requests.post(
                'http://localhost:8000/server-preferences/', 
                json=details,
                headers=headers
            )
            resdict[preference['name']] = res
    except Exception as e:
        logging.error(e)
        return e
    return resdict


def plugin_preferences_upload(obj, id):
    try:
        resdict = {}
        headers = {'Content-type': 'application/json'}
        for preference in obj:
            preference['policy_id'] = id
        
            if not preference.get('selectedValue'):
                preference['selectedValue'] = 'None'

            res = requests.post(
                'http://localhost:8000/plugin-preferences/', 
                json=preference,
                headers=headers
            )
            resdict[preference['pluginName']] = res
    except Exception as e:
        logging.error(e)
        return e
    return resdict


def server_and_plugins_upload(obj, id):
    try:
        server_preferences = obj['ServerPreferences']
        plugin_preferences = obj['PluginsPreferences']
        server_prefs = server_preferences_upload(server_preferences, id)
        plugin_prefs = plugin_preferences_upload(plugin_preferences, id)
    except Exception as e:
        logging.error(e)
        return e
    return {'sp': server_prefs, 'pp': plugin_prefs}


def family_selection_items_upload(obj, id):
    resdict = {}
    try:
        for item in obj:
            item['policy_id'] = id
            headers = {'Content-type': 'application/json'}
            res = requests.post(
                'http://localhost:8000/family-selection/', 
                json=item,
                headers=headers
            )
            resdict[item['FamilyName']] = res
    except Exception as e:
        return e
    return resdict


def individual_plugin_selection_items_upload(obj, id):
    resdict = {}
    try:
        for item in obj:
            item['policy_id'] = id
            headers = {'Content-type': 'application/json'}
            res = requests.post(
                'http://localhost:8000/individual-plugin-selection/', 
                json=item,
                headers=headers
            )
            resdict[item['PluginId']] = res
    except Exception as e:
        return e
    return resdict


def report_name_uploader(name, id):
    try:
        details = {
            'policy_id': id,
            'name': name
        }
        headers = {'Content-type': 'application/json'}
        res = requests.post(
            'http://localhost:8000/report/', 
            json=details,
            headers=headers
        )
    except Exception as e:
        return e
    return res


def report_host_uploader(name, id):
    try:
        details = {
            'policy_id': id,
            'name': name
        }
        headers = {'Content-type': 'application/json'}
        res = requests.post(
                'http://localhost:8000/report-host/', 
                json=details,
                headers=headers
            )
        logging.debug({'res': res, 'id': res.json()['data']['id']})
    except Exception as e:
        return e
    return {'res': res, 'id': res.json()['data']['id']}


def host_properties_uploader(obj, report_host_id):
    try:
        resdict = {}
        for tag, value in obj.items():
            details = {
                'report_host_id': report_host_id,
                'tag_name': tag,
                'tag_value': value
            }
            headers = {'Content-type': 'application/json'}
            res = requests.post(
                    'http://localhost:8000/host-properties/', 
                    json=details,
                    headers=headers
                )
            logging.debug(res)
            resdict[report_host_id] = res
    except Exception as e:
        return e
    return resdict


def report_item_uploader(obj, report_host_id):
    try:
        obj['report_host_id'] = report_host_id
        headers = {'Content-type': 'application/json'}
        res = requests.post(
            'http://localhost:8000/report-item/', 
            json=obj,
            headers=headers
        )
        logging.debug(obj)
    except Exception as e:
        return e
    return {'res': res, 'id': res.json()['data']['id']}


def report_item_properties_uploader(obj, report_item_id):
    try:
        resdict = {}
        for property_name, property_value in obj.items():
            details = {
                'report_item_id': report_item_id,
                'property_name': property_name,
                'property_value': property_value
            }
            headers = {'Content-type': 'application/json'}
            res = requests.post(
                'http://localhost:8000/report-item-properties/', 
                json=details,
                headers=headers
            )
            resdict[report_item_id] = res
    except Exception as e:
        return e
    return resdict


def report_section_uploader(obj, id):
    try:
        for name, details in obj.items():
            report_host = report_host_uploader(name, id)
            report_host_id = report_host['id']
            host_props, rep_items = details['host_properties'], details['report_items']
            host_properties = host_properties_uploader(host_props, report_host_id)

            resdict = {}
            x = 0
            for item in rep_items:
                x = x+1
                report_item = report_item_uploader(item['item_attrib'], report_host_id)
                report_item_id = report_item['id']
                report_item_property = report_item_properties_uploader(item['item_values'], report_item_id)
                resdict[x] = report_item_property

    except Exception as e:
        return e
    return resdict


def uploader_mapping():
    return {
        'policy': policy_upload,
        'server_and_plugins': server_and_plugins_upload,
        'family_selection_items': family_selection_items_upload,
        'individual_plugin_selection_items': individual_plugin_selection_items_upload,
        'report_name': report_name_uploader,
        'report_hosts': report_section_uploader
    }