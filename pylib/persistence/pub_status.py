#!/usr/bin/python

from BaseClasses import LampadasCollection
from base import Persistence

class PubStatus(Persistence):

    def __getattr__(self, attribute):
        if attribute=='documents':
            return self.dms.document.get_by_keys([['pub_status_code', '=', self.code]])

        if attribute in ('name', 'description'):
            self.name = LampadasCollection()
            self.description = LampadasCollection()
            i18ns = self.dms.pub_status_i18n.get_by_keys([['pub_status_code', '=', self.code]])
            for key in i18ns.keys():
                i18n = i18ns[key]
                self.name[i18n.lang] = i18n.pub_status_name
                self.description[i18n.lang] = i18n.pub_status_desc
        if attribute=='name':
            return self.name
        else:
            return self.description

