#!/usr/bin/python

from BaseClasses import LampadasCollection
from base import Persistence

class Type(Persistence):

    def __getattr__(self, attribute):
        if attribute=='documents':
            self.documents =self.dms.document.get_by_keys([['type_code', '=', self.code]])
            return self.documents
        elif attribute in ('name', 'description'):
            name = LampadasCollection()
            description = LampadasCollection()
            i18ns = self.dms.type_i18n.get_by_keys([['type_code', '=', self.code]])
            for key in i18ns.keys():
                i18n = i18ns[key]
                name[i18n.lang] = i18n.type_name
                description[i18n.lang] = i18n.type_desc
            if attribute=='name':
                return name
            else:
                return description
        else:
            raise AttributeError('No such attribute %s' % attribute)
