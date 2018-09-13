# -*- coding: utf-8 -*-

{
    'name': 'Quick Validate Receipt',
    'category': 'Stock',
    'version': '09.0.1.0.0',
    'summary': 'This module will validate multiple receipts with updated received quantity and source location.',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': 'AGPL-3',
    'description': 'Quickly validate multiple incoming stock with ease.',

    'depends': [
        'purchase',
        'stock'
    ],

    'data': [
        'wizard/stock_receipt_wizard_view.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'auto_install': False,
    'installable': True,
    'application': False

}
