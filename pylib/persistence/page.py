#!/usr/bin/python
# 
# This file is part of the Lampadas Documentation System.
# 
# Copyright (c) 2000, 2001, 2002 David Merrill <david@lupercalia.net>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# 

from BaseClasses import LampadasCollection
from base import Persistence

class Page(Persistence):

    def __getattr__(self, attribute):
        if attribute in ('title', 'menu_name', 'page', 'version'):
            self.title     = LampadasCollection()
            self.menu_name = LampadasCollection()
            self.page      = LampadasCollection()
            self.version   = LampadasCollection()
            i18ns = page_i18n.get_by_keys([['page_code', '=', self.code]])
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

