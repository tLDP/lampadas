#!/usr/bin/python

from BaseClasses import LampadasCollection
from base import Persistence

class News(Persistence):

    def __getattr__(self, attribute):
        if attribute=='untranslated_lang_keys':
            untranslated = []
            supported_langs = self.dms.language.get_by_keys([['supported', '=', 1]])
            for key in supported_langs.keys():
                if key not in self.headline.keys():
                    untranslated.append(key)
            return untranslated
        elif attribute in ('headline', 'news', 'version'):
            version = LampadasCollection()
            headline = LampadasCollection()
            news = LampadasCollection()
            i18ns = self.dms.news_i18n.get_by_keys([['news_id', '=', self.id]])
            for key in i18ns.keys():
                i18n = i18ns[key]
                version[i18n.lang] = i18n.version
                headline[i18n.lang] = i18n.headline
                news[i18n.lang] = i18n.news
            if attribute=='version':
                return version
            elif attribute=='headline':
                return headline
            else:
                return news
        else:
            raise AttributeError('No such attribute %s' % attribute)

