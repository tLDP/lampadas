from Globals import YES, NO
from base import DataManager

class Section(DataManager):

    def __init__(self):
        DataManager.__init__(self, 'section',
            {'section_code':        {'key_field': YES, 'data_type': 'string',   'nullable': NO,  'i18n': NO,  'foreign_key': '', 'attribute': 'code'},
             'sort_order':          {'key_field': NO,  'data_type': 'int',      'nullable': NO,  'i18n': NO,  'foreign_key': ''},
             'only_dynamic':        {'key_field': NO,  'data_type': 'bool',     'nullable': NO,  'i18n': NO,  'foreign_key': ''},
             'created':             {'key_field': NO,  'data_type': 'created',  'nullable': NO,  'i18n': NO,  'foreign_key': ''},
             'updated':             {'key_field': NO,  'data_type': 'updated',  'nullable': NO,  'i18n': NO,  'foreign_key': ''}})
