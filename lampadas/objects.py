#!/usr/bin/python

# Lampadas imports
from Config import config

# Twisted imports
from twisted.internet import reactor
from twisted.enterprise import adbapi, row, reflector
from twisted.enterprise.sqlreflector import SQLReflector
from twisted.python import usage
from twisted.cred.authorizer import DefaultAuthorizer
from twisted.internet import defer

# Sibling imports
from row import ROW_CLASSES


class Block:
    def __init__(self, refl):
        self.refl = refl

    def get_all(self, callback):
        self.refl.loadObjectsFrom('block').addCallback(callback)

    def get_by_code(self, code, callback):
        w = [('block_code', reflector.EQUAL, code)]
        self.refl.loadObjectsFrom('block', whereClause=w).addCallback(callback)

class Page:
    def __init__(self, refl):
        self.refl = refl

    def get_all(self, callback):
        self.refl.loadObjectsFrom('page').addCallback(callback)

    def get_by_code(self, code, callback):
        w = [('page_code', reflector.EQUAL, code)]
        self.refl.loadObjectsFrom('page', whereClause=w).addCallback(callback)

class Section:
    def __init__(self, refl):
        self.refl = refl

    def get_all(self, callback):
        self.refl.loadObjectsFrom('section').addCallback(callback)

    def get_by_code(self, code, callback):
        w = [('section_code', reflector.EQUAL, code)]
        self.refl.loadObjectsFrom('section', whereClause=w).addCallback(callback)

class String:
    def __init__(self, refl):
        self.refl = refl

    def get_all(self, callback):
        self.refl.loadObjectsFrom('string').addCallback(callback)

    def get_by_code(self, code, callback):
        w = [('string_code', reflector.EQUAL, code)]
        self.refl.loadObjectsFrom('string', whereClause=w).addCallback(callback)

class Objects:
    def connect(self, callback):
        if config.db_type=='pgsql':
            db_module = 'pyPgSQL.PgSQL'
        else:
            db_module = 'pyMySQL.MySQL'
        self.dbpool = adbapi.ConnectionPool(db_module, database=config.db_name, user='www-data')
        self.refl = SQLReflector(self.dbpool, ROW_CLASSES, callback)

        self.block = Block(self.refl)
        self.page = Page(self.refl)
        self.section = Section(self.refl)
        self.string = String(self.refl)

object_server = Objects()
