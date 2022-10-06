# -*- coding: utf-8 -*-
{
    'name': 'Thiết bị giáo dục',
    'version': '1',
    'category': 'Thiết bị giáo dục',
    'live_test_url': '#',
    'summary': 'Phần mềm quản lý - Thiết bị giáo dục',
    'author': 'Lv Quy',
    'company': 'Minh Nghĩa',
    'website': 'https://thietbiedu.vn',
    'depends': ['base_setup','website','website_blog'],
    'data': [
        #data

        # security
        # 'security/ir.model.access.csv',
        # views
        'views/hide_add_to_cart_btn.xml',
        'views/custom_footer.xml',

    ],

    'assets': {
        'web.assets_backend': [

        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],
    'license': 'AGPL-3',
}
