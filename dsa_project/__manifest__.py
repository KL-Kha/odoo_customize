# -*- coding: utf-8 -*-
{
    'name': "DSAgency Project",

    'summary': """
    Automatically send the email when assignee gets assigned to the task
    """,

    'description': """
    When assigning a person and saving the task, it will automatically send an email with specific information such as:
        • Project - Code
        • Priority
        • Planned Date ( Deadline if have )
    """,

    'author': "Jun Truong",
    'website': "https://www.dsagency.vn",

    'category': 'DSAgency/Utilities',
    'version': '16.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        'views/res_config_settings_views.xml',
        'data/mail_template_data.xml',
    ],
}
