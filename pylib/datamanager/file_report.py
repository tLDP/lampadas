from Globals import YES, NO
from base import DataManager

class FileReport(DataManager):

    def __init__(self):
        DataManager.__init__(self, 'file_report',
            {'report_code':         {'key_field': YES, 'data_type': 'string',   'nullable': NO,  'i18n': NO,  'foreign_key': '', 'attribute': 'code'},
             'only_cvs':            {'key_field': NO,  'data_type': 'bool',     'nullable': NO,  'i18n': NO,  'foreign_key': ''},
             'command':             {'key_field': NO,  'data_type': 'string',   'nullable': NO,  'i18n': NO,  'foreign_key': ''},
             'created':             {'key_field': NO,  'data_type': 'created',  'nullable': NO,  'i18n': NO,  'foreign_key': ''},
             'updated':             {'key_field': NO,  'data_type': 'updated',  'nullable': NO,  'i18n': NO,  'foreign_key': ''}})

    def synch(self):
        last_synched = self.last_synched
        super(FileReport, self).synch()

        # Synchronize with i18n cache.
        self.dms.file_report_i18n.synch()
        i18ns = self.dms.file_report_i18n.get_by_keys([['updated', '>=', last_synched]])
        for key in i18ns.keys():
            i18n = i18ns[key]
            mine = self.get_by_id(i18n.code)
            if hasattr(mine, 'i18n'):
                delattr(mine, 'i18n')
