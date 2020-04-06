ch = {
    'extend': None,

    'domain_name': r'Domain name:\s?(.+)',
    'registrar': r'Registrar:\s?(.+)',
    'registrant': r'Holder of domain name:\n\s*(.+)',

    'creation_date': None,
    'expiration_date': None,
    'updated_date': None,

    'name_servers': r'Name servers:\s*(.+)\s*',
    'status': None,
    'emails': None,
}

lu = {
    'extend': None,

    'domain_name': r'domainname:\s?(.+)',
    'registrar': r'registrar-name:\s?(.+)',
    'registrant': None,

    'creation_date': None,
    'expiration_date': None,
    'updated_date': None,

    'name_servers': r'\nnserver:\s*(.+)',
    'status': r'domaintype:\s?(.+)',
    'emails': None,
}

swiss = {
    'extend': 'com'
}

pt = {
    'extend': 'com',

    'domain_name': r'Domain:\s?(.+)',
    'registrar': r'Admin Name:\s?(.+)',
    'registrant': r'Owner:\s?(.+)',
    'creation_date': r'Creation Date:\s?(.+)',
    'expiration_date': r'Expiration Date:\s?(.+)',
    'updated_date': None,

    'name_servers': r'Name Server:\s*(.+)',
    'status': r'Domain Status::\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}'
}
