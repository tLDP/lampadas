#!/usr/bin/python

from BaseClasses import LampadasCollection
from base import Persistence

class Language(Persistence):

    def __getattr__(self, attribute):
        if attribute=='documents':
            return self.dms.document.get_by_keys([['lang', '=', self.code]])

        if attribute=='name':
            self.name = LampadasCollection()
            i18ns = self.dms.language_i18n.get_by_keys([['lang_code', '=', self.code]])
            for key in i18ns.keys():
                i18n = i18ns[key]
                self.name[i18n.lang] = i18n.lang_name
        if attribute=='name':
            return self.name
        else:
            raise AttributeError('No such attribute %s' % attribute)
