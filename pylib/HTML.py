#!/usr/bin/python

"""
Lampadas HTML Primitives Module

This module generates HTML primitives and web pages for the WWW front-end
to the Lampadas system.
"""

# Modules ##################################################################

import DataLayer


# Constants


# Globals

L = DataLayer.Lampadas()


# HTMLFactory

class HTMLFactory:

	def __init__(self):
		self.Page = PageFactory()
		self.Combo = ComboFactory()


# PageFactory

class PageFactory:

	def __call__(self, key, lang):
		page = L.Strings['tpl-default'].I18n[lang].Text
		page = page.replace('|header|', L.Strings['header'].I18n[lang].Text)
		page = page.replace('|footer|', L.Strings['footer'].I18n[lang].Text)
		
		
		if key[:4] == 'doc/':
			docid = int(key[4:])
			print "DOC " + str(docid) + " requested"
			Doc = L.Docs[docid]
			assert not Doc == None
			Files = Doc.Files
			keys = Files.keys()
			for key in keys:
				File = Files[key]
				print "filename: " + File.Filename
				print "format: " + File.Format
		else:
			page = page.replace('|body|', L.Strings[key].I18n[lang].Text)
		return page



# ComboFactory

class ComboFactory:

	def Classes(self, value, lang):

		self.combo = "<select name='class'>\n"
		keys = L.Classes.keys()
		for key in keys:
			classfoo = L.Classes[key]
			if classfoo == None: break
			self.combo = self.combo + "<option "
			if classfoo.ID == value:
				self.combo = self.combo + "selected "
			self.combo = self.combo + "value='" + str(classfoo.ID) + "'>"
			self.combo = self.combo + classfoo.I18n[lang].Name
			self.combo = self.combo + "</option>\n"
		self.combo = self.combo + "</select>"
		return self.combo

	def Docs(self, value, lang=None):
		self.combo = "<select name='doc'>\n"
		keys = L.Docs.keys()
		for key in keys:
			doc = L.Docs[key]
			if doc == None: break
			if doc.LanguageCode == lang or lang == None:
				self.combo = self.combo + "<option "
				if doc.ID == value:
					self.combo = self.combo + "selected "
				self.combo = self.combo + "value='" + str(doc.ID) + "'>"
				self.combo = self.combo + doc.Title
				self.combo = self.combo + "</option>\n"
		self.combo = self.combo + "</select>"
		return self.combo


Factory = HTMLFactory()

#output = Factory.Combo.Classes(2,'EN')
#print output

#output = Factory.Page('pg-about', 'EN')
#print output

output = Factory.Page('doc/1', 'EN')
#print output

#if __name__ == "__main__":
