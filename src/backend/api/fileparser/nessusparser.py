import xml.etree.ElementTree as et


def parse(file):
    tree = et.parse(file)
    root = tree.getroot()
    policy_report = dictify(root)
    policy, report = dictify(policy_report['Policy']), dictify(policy_report['Report'])
    p_name, p_comments = if_exists(policy.get('policyName')), if_exists(policy.get('policyComments'))
    preferences, family_selection, individual_plugin_selection =    policy.get('Preferences'), \
                                                                    policy.get('FamilySelection'), \
                                                                    policy.get('IndividualPluginSelection')
    server_and_plugins = {key: parse_section(value) for key, value in dictify(preferences).items()}
    family_selection_items = parse_section(family_selection)
    individual_plugin_selection_items = parse_section(individual_plugin_selection)

    report_name = policy_report['Report'].attrib['name']
    report_hosts = {item.attrib['name']: [val for val in item] for item in policy_report['Report']}
    report_hosts = expand_hosts(report_hosts)

    return {
        'policy': [p_name, p_comments],
        'server_and_plugins': server_and_plugins,
        'family_selection_items': family_selection_items,
        'individual_plugin_selection_items': individual_plugin_selection_items,
        'report_name': report_name,
        'report_hosts': report_hosts
    }


def parse_section(obj):
    return [{value.tag: str(value.text) for value in item} for item in obj] if obj is not None else 'None'


def dictify(obj):
    return {val.tag: obj.find(val.tag) for val in obj}


def if_exists(obj):
    return obj.text if obj is not None else 'None'


def host_properties(obj):
    return {item.attrib['name']: item.text for item in obj}


def report_item(obj):
    return [{'Attrib': obj.attrib}, {'Values': {item.tag: item.text for item in obj}}]


def expand_hosts(obj):
    for key, value in obj.items():
        report_h, report_items = {}, []
        for item in value:
            if item.tag == 'HostProperties':
                report_h['host_properties'] = host_properties(item)
            else:
                report_items.append({'item_attrib': item.attrib, 'item_values': {i.tag: i.text for i in item}})
        report_h['report_items'] = report_items
        obj[key] = report_h
    return obj

