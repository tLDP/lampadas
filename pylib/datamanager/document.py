from Globals import YES, NO
from base import DataManager

class Document(DataManager):

    def __init__(self):
        DataManager.__init__(self, 'document',
            {'doc_id':              {'key_field': YES, 'data_type': 'sequence', 'nullable': NO,  'i18n': NO,  'foreign_key': '', 'attribute': 'id'},
             'lang':                {'key_field': NO,  'data_type': 'string',   'nullable': NO,  'i18n': NO,  'foreign_key': 'language.lang_code'},
             'title':               {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'short_title':         {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'type_code':           {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': 'type.type_code'},
             'format_code':         {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': 'format.format_code'},
             'dtd_code':            {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': 'dtd.dtd_code'},
             'dtd_version':         {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'version':             {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'last_update':         {'key_field': NO,  'data_type': 'date',     'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'isbn':                {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'pub_status_code':     {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': 'pub_status.pub_status_code'},
             'review_status_code':  {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': 'review_status.review_status_code'},
             'maintained':          {'key_field': NO,  'data_type': 'bool',     'nullable': NO,  'i18n': NO,  'foreign_key': ''},
             'maintainer_wanted':   {'key_field': NO,  'data_type': 'bool',     'nullable': NO,  'i18n': NO,  'foreign_key': ''},
             'license_code':        {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'license_version':     {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'copyright_holder':    {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'abstract':            {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'short_desc':          {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'rating':              {'key_field': NO,  'data_type': 'int',      'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'sk_seriesid':         {'key_field': NO,  'data_type': 'string',   'nullable': NO,  'i18n': NO,  'foreign_key': ''},
             'replaced_by_id':      {'key_field': NO,  'data_type': 'int',      'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'lint_time':           {'key_field': NO,  'data_type': 'time',     'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'mirror_time':         {'key_field': NO,  'data_type': 'time',     'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'pub_time':            {'key_field': NO,  'data_type': 'time',     'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'first_pub_date':      {'key_field': NO,  'data_type': 'date',     'nullable': YES, 'i18n': NO,  'foreign_key': ''},
             'encoding':            {'key_field': NO,  'data_type': 'string',   'nullable': YES, 'i18n': NO,  'foreign_key': 'encoding.encoding'},
             'created':             {'key_field': NO,  'data_type': 'created',  'nullable': NO,  'i18n': NO,  'foreign_key': ''},
             'updated':             {'key_field': NO,  'data_type': 'updated',  'nullable': NO,  'i18n': NO,  'foreign_key': ''}})
