#!/usr/bin/python

from BaseClasses import LampadasCollection
from base import Persistence

class Page(Persistence):

    def __getattr__(self, attribute):
        if attribute=='template':
            return self.dms.template.get_by_id(self.template_code)
            
        if attribute in ('title', 'menu_name', 'page', 'version'):
            self.title     = LampadasCollection()
            self.menu_name = LampadasCollection()
            self.page      = LampadasCollection()
            self.version   = LampadasCollection()
            i18ns = self.dms.page_i18n.get_by_keys([['page_code', '=', self.code]])
            for key in i18ns.keys():
                i18n = i18ns[key]
                self.title[i18n.lang]     = i18n.title
                self.menu_name[i18n.lang] = i18n.menu_name
                self.page[i18n.lang]      = i18n.page
                self.version[i18n.lang]   = i18n.version
        if attribute=='title':
            return self.title
        elif attribute=='menu_name':
            return self.menu_name
        elif attribute=='page':
            return self.page
        else:
            return self.version

