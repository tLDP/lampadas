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

from BaseClasses import *

class DocCollections(DataCollection):
    """
    A collection object providing access to document collections.
    """

    def __init__(self, doc_id=0):
        DataCollection.__init__(self, None, DocCollection,
                                 'document_collection',
                                 [{'doc_id':          {'data_type': 'int'}},
                                  {'collection_code': {'data_type': 'string'}}],
                                 [{'created':  {'data_type': 'created'}},
                                  {'updated':  {'data_type': 'updated'}}],
                                 [])

class DocCollection(DataObject):
    """
    A collection for the document.
    """
    pass

doccollections = DocCollections()
doccollections.load()

