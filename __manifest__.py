{
    'name': 'Bakery Custom Report',
    'version': '1.0',
    'summary': 'Custom POS Receipt for Bakery with Print POS Order button',
    'category': 'Point of Sale',
    'author': 'Your Name',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'bakery_custom_report/static/src/js/HeaderScreen.js',
            'bakery_custom_report/static/src/js/CustomOrderReceipt.js',
            'bakery_custom_report/static/src/js/ReprintReceiptScreen.js',
            'bakery_custom_report/static/src/xml/OrderHeader.xml',
            'bakery_custom_report/static/src/xml/OrderReceipt.xml',
        ],
    },
    'installable': True,
    'application': False,
}
