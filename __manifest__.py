{
    'name': "Awesome Owl",
    'description': """
        Tutorials for the beginning to domain the owl framework
    """,
    'summary': "Making a route to display an intro to odoo web framwework",
    'category': "Owl/Awesome",
    'author': "Amilton Bandeira",
    'odoo-version': "18.0",
    'depends': [
        'web',
    ],
    'data': [
        '',
    ],
    'assets': {
        'web.assets_backend': [
            'awesome_owl/static/src/component.js',
            'awesome_owl/static/src/component.xml',
        ],
    },
    'license': "AGPL-3",
    'installble': True,
    'application': True,
    'auto_install': False,
}