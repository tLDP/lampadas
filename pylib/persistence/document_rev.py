#!/usr/bin/python

from base import Persistence

class DocumentRev(Persistence):

    def __getattr__(self, attribute):
        if attribute=='document':
            return self.dms.document.get_by_id(self.doc_id)
