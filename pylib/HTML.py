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
"""
Lampadas HTML Primitives Module

This module generates HTML primitives and web pages for the WWW front-end
to the Lampadas system.

FIXME: string concatenation is kinda slow. Use class WOStringIO instead.
As in

buf = WOStringIO()
buf.write('some piece of <HTML>')
buf.write('some other %s' % 'variable-value')
buf.get_value()

N.B: same interface as StringIO.

--nico
"""

class WOStringIO :
    "Write-Only pure python extra fast buffer"

    def __init__(self,s='') :
        self.data = [s]

    def write(self,s) :
        self.data.append(s)

    def get_value(self) :
        return ''.join(self.data)
    
# Modules ##################################################################

from Globals import *
from Config import config
from Log import log
from URLParse import URI
from DataLayer import lampadas
from WebLayer import lampadasweb
from Sessions import sessions

import commands
from string import split
import sys
import os


# Globals


# Constants

EDIT_ICON = '<img src="images/edit.png" alt="Edit" height="20" width="20" border="0" hspace="5" vspace="0" align="top">'


# ComboFactory

class ComboFactory:

    def tf(self, name, value, lang):
        log(3, 'creating tf combo: ' + name + ', value is: ' + str(value))
        combo = '<select name="' + name + '">\n'
        if value==1:
            combo = combo + '<option selected value="1">|stryes|</option>\n'
            combo = combo + '<option value="0">|strno|</option>\n'
        else:
            combo = combo + '<option value="1">|stryes|</option>\n'
            combo = combo + '<option selected value="0">|strno|</option>\n'
        combo = combo + '</select>\n'
        return combo

    def stylesheet(self, value):
        combo = '<select name="stylesheet">\n'
        combo = combo + '</select>\n'
        return combo
    
    def type(self, value, lang):
        combo = "<select name='type_code'>\n"
        keys = lampadas.types.sort_by('sort_order')
        for key in keys:
            type = lampadas.types[key]
            assert not type==None
            combo = combo + "<option "
            if type.code==value:
                combo = combo + "selected "
            combo = combo + "value='" + type.code + "'>"
            combo = combo + type.name[lang]
            combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo

    def doc(self, value, lang):
        combo = "<select name='doc'>\n"
        keys = lampadas.Docs.sort_by_lang('Title', lang)
        for key in keys:
            doc = lampadas.Docs[key]
            assert not doc==None
            if doc.Lang==lang or lang==None:
                combo = combo + "<option "
                if doc.ID==value:
                    combo = combo + "selected "
                combo = combo + "value='" + str(doc.ID) + "'>"
                combo = combo + doc.Title
                combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo

    def sk_seriesid(self, value, lang):
        combo = "<select name='sk_seriesid'>\n"
        keys = lampadas.Docs.sort_by_lang('Title', lang)
        for key in keys:
            doc = lampadas.Docs[key]
            assert not doc==None
            if doc.Lang==lang or lang==None:
                combo = combo + "<option "
                if doc.sk_seriesid==value:
                    combo = combo + "selected "
                combo = combo + "value='" + str(doc.sk_seriesid) + "'>"
                combo = combo + doc.Title
                combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo

    def dtd(self, value, lang):
        combo = "<select name='dtd'>\n"
        keys = lampadas.DTDs.sort_by_lang('DTD', lang)
        for key in keys:
            dtd = lampadas.DTDs[key]
            assert not dtd==None
            combo = combo + "<option "
            if dtd.DTD==value:
                combo = combo + "selected "
            combo = combo + "value='" + dtd.DTD + "'>"
            combo = combo + dtd.DTD
            combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo
    
    def format(self, value, lang):
        combo = "<select name='format'>\n"
        keys = lampadas.Formats.sort_by_lang('name', lang)
        for key in keys:
            format = lampadas.Formats[key]
            assert not format==None
            combo = combo + "<option "
            if format.ID==value:
                combo = combo + "selected "
            combo = combo + "value='" + str(format.ID) + "'>"
            combo = combo + format.name[lang]
            combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo

    def language(self, value, lang):
        combo = "<select name='lang'>\n"
        keys = lampadas.languages.sort_by_lang('name', lang)
        for key in keys:
            language = lampadas.languages[key]
            assert not language==None
            combo = combo + "<option "
            if language.code==value:
                combo = combo + "selected "
            combo = combo + "value='" + language.code + "'>"
            combo = combo + language.name[lang]
            combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo

    def license(self, value, lang):
        combo = "<select name='license_code'>\n"
        keys = lampadas.licenses.sort_by('sort_order')
        for key in keys:
            license = lampadas.licenses[key]
            assert not license==None
            combo = combo + "<option "
            if license.license_code==value:
                combo = combo + "selected "
            combo = combo + "value='" + license.license_code + "'>"
            combo = combo + license.short_name[lang]
            combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo

    def page(self, value, lang):
        combo = "<select name='page_code'>\n"
        keys = lampadasweb.pages.sort_by('page_code')
        for key in keys:
            page = lampadasweb.pages[key]
            assert not page==None
            combo = combo + "<option "
            if Page.Code==value:
                combo = combo + "selected "
            combo = combo + "value='" + str(page.Code) + "'>"
            combo = combo + page.title[lang]
            combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo

    def pub_status(self, value, lang):
        combo = "<select name='pub_status_code'>\n"
        keys = lampadas.PubStatuses.sort_by('sort_order')
        for key in keys:
            PubStatus = lampadas.PubStatuses[key]
            assert not PubStatus==None
            combo = combo + "<option "
            if PubStatus.Code==value:
                combo = combo + "selected "
            combo = combo + "value='" + str(PubStatus.Code) + "'>"
            combo = combo + PubStatus.name[lang]
            combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo
        
    def review_status(self, value, lang):
        combo = "<select name='review_status_code'>\n"
        keys = lampadas.ReviewStatuses.sort_by('sort_order')
        for key in keys:
            ReviewStatus = lampadas.ReviewStatuses[key]
            assert not ReviewStatus==None
            combo = combo + "<option "
            if ReviewStatus.Code==value:
                combo = combo + "selected "
            combo = combo + "value='" + str(ReviewStatus.Code) + "'>"
            combo = combo + ReviewStatus.name[lang]
            combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo

    def tech_review_status(self, value, lang):
        combo = "<select name='tech_review_status_code'>\n"
        keys = lampadas.ReviewStatuses.sort_by('sort_order')
        for key in keys:
            ReviewStatus = lampadas.ReviewStatuses[key]
            assert not ReviewStatus==None
            combo = combo + "<option "
            if ReviewStatus.Code==value:
                combo = combo + "selected "
            combo = combo + "value='" + str(ReviewStatus.Code) + "'>"
            combo = combo + ReviewStatus.name[lang]
            combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo

    def subtopic(self, value, lang):
        combo = '<select name="subtopic_code">\n'
        keys = lampadas.Subtopics.sort_by('sort_order')
        for key in keys:
            subtopic = lampadas.subtopics[key]
            assert not subtopic==None
            combo = combo + "<option "
            if subtopic.code==value:
                combo = combo + "selected "
            combo = combo + "value='" + str(subtopic.code) + "'>"
            combo = combo + subtopic.name[lang]
            combo = combo + "</option>\n"
        combo = combo + "</select>"
        return combo


class TableFactory:

    def bar_graph(self, value, max, lang):
        return str(value) + '/' + str(max)

    def doc(self, uri):
        if uri.id:
            doc = lampadas.Docs[uri.id]
            box = '<form method=GET action="data/save/document" name="document">'
        else:
            doc = Doc()
            box = '<form method=GET action="data/save/newdocument" name="document">'
        box = box + '<input name="doc_id" type=hidden value=' + str(doc.ID) + '>\n'
        
        box = box + '<table class="box"><tr><th colspan="6">|strdocdetails|</th></tr>'
        box = box + '<tr>\n'
        box = box + '<th class="label">|strtitle|</th><td colspan=5><input type=text name="title" size=60 style="width:100%" value="' + doc.Title + '"></td>\n'
        box = box + '</tr>\n'
        box = box + '<tr>\n'
        box = box + '<th class="label">'
        if doc.URL:
            box = box + '<a href="' + doc.URL + '">|strurl|</a>'
        else:
            box = box + '|strurl|'
        box = box + '</th><td colspan=5><input type=text name="url" size=60 style="width:100%" value="' + doc.URL + '"></td>'
        box = box + '</tr>\n<tr>\n'
        box = box + '<th class="label">'

        if doc.HomeURL:
            box = box + '<a href="' + doc.HomeURL + '">|strhome_url|</a>'
        else:
            box = box + '|strhome_url|'
        box = box + '</th><td colspan=5><input type=text name="ref_url" size=60 style="width:100%" value="' + doc.HomeURL + '"></td>'
        box = box + '</tr>\n<tr>\n'
        box = box + '<th class="label">|strstatus|</th><td>'
        box = box + combo_factory.pub_status(doc.PubStatusCode, uri.lang)
        box = box + '</td>\n'
        box = box + '<th class="label">|strtype|</th><td>\n'
        box = box + combo_factory.type(doc.type_code, uri.lang)
        box = box + '</td>\n'
        box = box + '<th class="label">|strmaintained|</th><td>\n'
        if doc.Maintained:
            box = box + '|stryes|'
        else:
            box = box + '|strno|'
        box = box + '</td>'
        box = box + '</tr>\n<tr>\n'
        box = box + '<th class="label">|strwriting|</th><td>'
        box = box + combo_factory.review_status(doc.ReviewStatusCode, uri.lang)
        box = box + '</td>\n'
        box = box + '<th class="label">|straccuracy|</th><td>'
        box = box + combo_factory.tech_review_status(doc.TechReviewStatusCode, uri.lang)
        box = box + '</td>\n'
        box = box + '<th class="label">|strlicense|</th><td>'
        box = box + combo_factory.license(doc.license_code, uri.lang)
        box = box + '</td>'
        box = box + '</tr>\n<tr>\n'
        box = box + '<th class="label">|strpub_date|</th><td><input type=text name="pub_date" size=10 value="' + doc.PubDate + '"></td>'
        box = box + '<th class="label">|strupdated|</th><td><input type=text name="last_update" size=10 value="' + doc.LastUpdate + '"></td>'
        box = box + '<th class="label">|strversion|</th><td><input type=text name="version" size=10 value="' + doc.Version + '"></td>'
        box = box + '</tr>\n<tr>\n'
        box = box + '<th class="label">|strtickle_date|</th><td><input type=text name="tickle_date" size=10 value="' + doc.TickleDate + '"></td>'
        box = box + '<th class="label">|strisbn|</th><td><input type=text name="isbn" size=14 value="' + doc.ISBN + '"></td>'
        box = box + '<th class="label">|strrating|</th>\n'
        box = box + '<td>'
        box = box + self.bar_graph(doc.Rating, 10, uri.lang)
        box = box + '</td>\n'
        box = box + '</tr>\n<tr>\n'
        box = box + '<th class="label">|strformat|</th><td>'
        box = box + lampadas.Formats[doc.format_code].name[uri.lang]
        box = box + '</td>'
        box = box + '<th class="label">|strdtd|</th><td>'
        box = box + doc.DTD + ' ' + doc.DTDVersion
        box = box + '</td>'
        box = box + '<th class="label">|strlanguage|</th><td>'
        box = box + combo_factory.language(doc.Lang, uri.lang)
        box = box + '</td>'
        box = box + '</tr>\n<tr>\n'
        box = box + '<th class="label">|strmaintainer_wanted|</th><td>' + combo_factory.tf('maintainer_wanted', doc.maintainer_wanted, uri.lang) + '</td>\n'
        box = box + '<td></td><td></td>'
        box = box + '</tr>\n<tr>\n'
        box = box + '<th class="label">|strabstract|</th>'
        box = box + '<td colspan=5><textarea name="abstract" rows=6 cols=40 style="width:100%" wrap>' + doc.Abstract + '</textarea></td>\n'
        box = box + '</tr>\n'
        box = box + '<tr><td></td><td><input type=submit name="save" value="|strsave|"></td></tr>\n'
        box = box + '</table>\n'
        box = box + '</form>\n'

        return box

    def cvslog(self, uri):
        doc = lampadas.Docs[uri.id]
        box = '<table class="box">\n'
        box = box + '<tr><th>|strcvslog|</th></tr>\n'
        box = box + '<tr><td>\n'
        cvsdir = config.cvs_root + str(doc.id)

        # FIXME: finish this.

        box = box + '</td></tr>\n'
        box = box + '</table>\n'
        return box

    def user(self, uri):
        box = '<table class="box">\n'
        if uri.username > '':
            user = lampadas.users[uri.username]
            box = box + '<form method=GET action="data/save/user" name="user">\n'
        else:
            user = User()
            box = box + '<form method=GET action="data/save/newuser" name="user">\n'
        box = box + '<input name="username" type=hidden value=' + uri.username + '></input>\n'
        box = box + '<tr><th colspan=2>|struserdetails|</th><th>|strcomments|</th></tr>\n'
        box = box + '<tr><th class="label">|strusername|</th><td>' + uri.username + '</td>\n'
        box = box + '<td rowspan=10 style="width:100%"><textarea name="notes" wrap=soft style="width:100%; height:100%">' + user.notes + '</textarea></td></tr>\n'
        box = box + '<tr><th class="label">|strfirst_name|</th><td><input type=text name=first_name value="' + user.first_name + '"></input></td></tr>\n'
        box = box + '<tr><th class="label">|strmiddle_name|</th><td><input type=text name=middle_name value="' + user.middle_name + '"></input></td></tr>\n'
        box = box + '<tr><th class="label">|strsurname|</th><td><input type=text name=surname value="' + user.surname + '"></input></td></tr>\n'
        box = box + '<tr><th class="label">|stremail|</th><td><input type=text name=email value="' + user.email + '"></input></td></tr>\n'
        box = box + '<tr><th class="label">|strstylesheet|</th><td><input type=text name=stylesheet value="' + user.stylesheet + '"></input></td></tr>\n'
        box = box + '<tr><th class="label">|strnewpassword|</th><td><input type=text name=password></input></td></tr>\n'
        box = box + '<tr><th class="label">|stradmin|</th><td>' + combo_factory.tf('admin', user.admin, uri.lang) + '</td></tr>\n'
        box = box + '<tr><th class="label">|strsysadmin|</th><td>' + combo_factory.tf('sysadmin', user.sysadmin, uri.lang) + '</td></tr>\n'
        box = box + '<tr><td></td><td><input type=submit name=save value=Save></td></tr>\n'
        box = box + '</form>\n'
        box = box + '</table>\n'
        return box
        
    def doctable(self, uri, user, type_code=None, subtopic_code=None):
        log(3, "Creating doctable")
        box = '<table class="box"><tr><th colspan="2">|strtitle|</th></tr>'
        keys = lampadas.Docs.sort_by("Title")
        for key in keys:
            doc = lampadas.Docs[key]
            if doc.Lang==uri.lang:
                ok = 1
                if type_code and doc.type_code <> type_code:
                    ok = 0
                if subtopic_code:
                    subtopic = lampadas.subtopics[subtopic_code]
                    if subtopic.docs[doc.ID]==None:
                        ok = 0
                if ok > 0:
                    box = box + '<tr><td>'
                    if user and user.can_edit(doc_id=doc.ID):
                        box = box + '<a href="editdoc/' + str(doc.ID) + '/">' + EDIT_ICON + '</a>'
                    box = box + '</td>\n'
                    box = box + '<td style="width:100%"><a href="doc/' + str(doc.ID) + '/">' + doc.Title + '</a></td>'
                    box = box + '</tr>\n'
        box = box + '</table>'
        return box

    def section_menu(self, uri, user, section_code):
        log(3, "Creating section menu: " + section_code)
        section = lampadasweb.sections[section_code]
        box = '<table class="navbox"><tr><th>' + section.name[uri.lang] + '</th></tr>\n'
        box = box + '<tr><td>'
        keys = lampadasweb.pages.sort_by('sort_order')
        for key in keys:
            page = lampadasweb.pages[key]
            if page.section_code==section.code:
                if page.only_registered or page.only_admin or page.only_sysadmin > 0:
                    if user==None:
                        continue
                if page.only_admin > 0:
                    if user.admin==0 and user.sysadmin==0:
                        continue
                if page.only_sysadmin > 0:
                    if user.sysadmin==0:
                        continue
                box = box + '<a href="' + page.code + '">' + page.menu_name[uri.lang] + '</a><br>\n'
        box = box + '</td></tr></table>\n'
        return box

    def section_menus(self, uri, user):
        log(3, "Creating all section menus")
        box = ''
        keys = lampadasweb.sections.sort_by('sort_order')
        for key in keys:
            section = lampadasweb.sections[key]
            if section.only_registered or section.only_admin or section.only_sysadmin > 0:
                if user==None or section.registered_count==0:
                    continue
            if section.only_admin > 0:
                if (user.admin==0 and user.sysadmin==0) or (section.admin_count==0):
                    continue
            if section.only_sysadmin > 0:
                if user.sysadmin==0 or section.sysadmin_count==0:
                    continue
            box = box + self.section_menu(uri, user, section.code)
        return box

    def recent_news(self, uri):
        log(3, 'Creating recent news')
        box = '<table class="box"><tr><th>|strdate|</th><th>|strnews|</th></tr>\n'
        keys = lampadasweb.news.sort_by_desc('pub_date')
        for key in keys:
            news = lampadasweb.news[key]
            if not news.news[uri.lang]==None:
                box = box + '<tr>\n'
                box = box + '<td>' + news.pub_date + '</td>\n'
                box = box + '<td>' + news.news[uri.lang] + '</td>\n'
                box = box + '</tr>\n'
        box = box + '</table>\n'
        return box

    def topics(self, uri):
        log(3, 'Creating topics table')
        box = '<table class="navbox"><tr><th>|strtopics|</th></tr>\n'
        box = box + '<tr><td><ol>\n'
        keys = lampadas.topics.sort_by('num')
        for key in keys:
            topic = lampadas.topics[key]
            box = box + '<li><a href="topic/' + topic.code + '">\n'
            box = box + topic.name[uri.lang] + '</a>\n'
        box = box + '</ol></td></tr>\n'
        box = box + '</table>\n'
        return box

    def subtopics(self, uri):
        log(3, 'Creating subtopics table')
        topic = lampadas.topics[uri.code]
        box = '<table class="navbox"><tr><th>' + topic.name[uri.lang] + '</th></tr>\n'
        box = box + '<tr><td>|topic.description|</td></tr>\n'
        box = box + '<tr><td><ol>\n'
        keys = lampadas.subtopics.sort_by('num')
        for key in keys:
            subtopic = lampadas.subtopics[key]
            if subtopic.topic_code==uri.code:
                box = box + '<li><a href="subtopic/' + subtopic.code + '">\n'
                box = box + subtopic.name[uri.lang] + '</a>\n'
        box = box + '</ol></td></tr>\n'
        box = box + '</table>\n'
        return box

    def subtopic(self, uri):
        log(3, 'Creating subtopic table')
        subtopic = lampadas.subtopics[uri.code]
        box = '<table class="navbox"><tr><th>' + subtopic.name[uri.lang] + '</th></tr>\n'
        box = box + '<tr><td>' + subtopic.description[uri.lang] + '</td></tr>\n'
        box = box + '<tr><td><ol>\n'
        keys = subtopic.docs.sort_by('Title')
        for key in keys:
            doc = subtopic.docs[key]
            if doc.subtopic.topic_code==uri.code and doc.Lang==uri.lang:
                box = box + '<li><a href="/doc/' + str(doc.ID) + '">\n'
                box = box + doc.Title + '</a>\n'
        box = box + '</ol></td></tr>\n'
        box = box + '</table>\n'
        return box

    def types(self, uri):
        log(3, 'Creating types table')
        box = '<table class="navbox"><tr><th>|strtypes|</th></tr>\n'
        box = box + '<tr><td>\n'
        keys = lampadas.types.sort_by('sort_order')
        for key in keys:
            type = lampadas.types[key]
            box = box + '<a href="type/' + type.code + '">\n'
            box = box + type.name[uri.lang] + '</a><br>\n'
        box = box + '</td></tr>\n'
        box = box + '</table>\n'
        return box

    def login(self, uri, user):
        if user:
            log(3, 'Creating active user box')
            box = '<table class="navbox"><tr><th>|stractive_user|</th></tr>\n'
            box = box + '<form name="logout" action="data/session/logout">\n'
            box = box + '<input name=username type=hidden value="' + user.username + '">\n'
            box = box + '<tr><td align=center>|session_name|</td></tr>\n'
            box = box + '<tr><td align=center><input type=submit name=logout value="|strlog_out|"></td></tr>\n'
            box = box + '</form>\n'
            box = box + '</table>\n'
        else:
            log(3, 'Creating login box')
            box = '<table class="navbox"><tr><th colspan="2">|strlogin|</th></tr>\n'
            box = box + '<form name="login" action="data/session/login" method=GET>\n'
            box = box + '<tr><th class="label">|strusername|</td><td><input type=text size=12 name=username></input></td></tr>\n'
            box = box + '<tr><th class="label">|strpassword|</td><td><input type=password size=12 name=password></input></td></tr>\n'
            box = box + '<tr><td align=center colspan=2><input type=submit name="login" value="login"><br>\n'
            box = box + '<a href="mailpass">|strmail_passwd|</a><br>\n'
            box = box + '<a href="newuser">|strcreate_acct|</a></td></tr>\n'
            box = box + '</form>\n'
            box = box + '</table>\n'
        return box

    def sessions(self, uri, user):
        if user:
            if user.admin > 0:
                log(3, 'Creating sessions table')
                box = '<table class="navbox"><tr><th>|strsessions|</th></tr>\n'
                box = box + '<tr><td>\n'
                keys = sessions.sort_by('username')
                for key in keys:
                    session = sessions[key]
                    box = box + '<a href="user/' + str(session.username) + '">\n'
                    user = lampadas.users[key]
                    box = box + user.name + '</a><br>\n'
                box = box + '</td></tr>\n'
                box = box + '</table>\n'
                return box
        return ' '

    def languages(self, uri):
        log(3, 'Creating languages table')
        box = '<table class="navbox"><tr><th>|strlanguages|</th></tr>\n'
        box = box + '<tr><td>\n'
        keys = lampadas.languages.sort_by_lang('name', uri.lang)
        for key in keys:
            language = lampadas.languages[key]
            if language.supported > 0:
                box = box + '<a href="/' + language.code + '/' + uri.base + '">' + language.name[uri.lang] + '</a><br>\n'
        box = box + '</td></tr>\n'
        box = box + '</table>\n'
        return box


    def user_docs(self, uri, user):
        log(3, 'Creating user_docs table')
        box = '<table class="navbox"><tr><th>|session_name|</th></tr>\n'
        keys = user.docs.sort_by_lang('Title', uri.lang)
        for key in keys:
            box = box + '<tr><td>\n'
            userdoc = user.docs[key]
            box = box + '<a href="/doc/' + userdoc.ID + '">' + usrdoc.title[uri.lang] + '</a>\n'
            box = box + '</td></tr>\n'
        box = box + '</table>\n'
        return box


# PageFactory

class PageFactory:

    tablef  = TableFactory()

    def page_exists(self, key):
        uri = URI(key)
        if uri.path=='' and lampadasweb.pages[uri.filename]:
            return 1
        return

    def page(self, key, session_id=''):
        uri = URI(key)
        build_user = None
        if session_id > '':
            username = lampadas.users.find_session_user(session_id)
            if username > '':
                build_user = lampadas.users[username]
                log(3, 'build_user: ' + build_user.username)

        log(3, 'Serving language ' + uri.lang)

        page = lampadasweb.pages[uri.filename]
        if page==None:
            page = lampadasweb.pages['404']
        assert not page==None
        html = self.build_page(page, uri, build_user)

        return html
    

    def build_page(self, page, uri, build_user):
        template = lampadasweb.templates[page.template_code]
        assert not template==None
        html = template.template

        html = html.replace('\|', 'DCM_PIPE')
    
        pos = html.find('|')
        while pos <> -1 :
            pos2 = html.find('|', pos+1)
            if pos2==-1:
                pos = -1
            else:
                oldstring = html[pos:pos2+1]
                token = html[pos+1:pos2]

                newstring = ''
            
                # Tokens based on a logged-in user
                # 
                if token=='session_id':
                    if build_user==None:
                        newstring = ''
                    else:
                        newstring = build_user.session_id
                if token=='session_username':
                    if build_user==None:
                        newstring = ''
                    else:
                        newstring = build_user.username
                if token=='session_name':
                    if build_user==None:
                        newstring = ''
                    else:
                        newstring = build_user.name
                if token=='session_user_docs':
                    newstring = self.tablef.user_docs(uri, build_user)

                # Meta-data about the page being served
                # 
                if token=='title':
                    newstring = page.title[uri.lang]
                if token=='body':
                    newstring = page.page[uri.lang]
                if token=='base':
                    newstring = 'http://' + config.hostname
                    if config.port > '':
                        newstring = newstring + ':' + config.port
                    newstring = newstring + config.root_dir
                    if uri.force_lang:
                        newstring = newstring + uri.lang + '/'
                if token=='uri.code':
                    newstring = uri.code
                if token=='uri.base':
                    newstring = uri.base


                # Configuration information
                # 
                if token=='hostname':
                    newstring = config.hostname
                if token=='rootdir':
                    newstring = config.root_dir
                if token=='port':
                    newstring = str(config.port)
                if token=='stylesheet':
                    newstring='default'
                if token=='version':
                    newstring = VERSION

                # Tokens for when a page embeds an object
                # 
                if token=='user.username':
                    user = lampadas.users[uri.username]
                    newstring = user.username
                if token=='user.name':
                    user = lampadas.users[uri.username]
                    newstring = user.name
                if token=='type.name':
                    type = lampadas.types[uri.code]
                    newstring = type.name[uri.lang]
                if token=='topic.name':
                    topic = lampadas.topics[uri.code]
                    newstring = topic.name[uri.lang]
                if token=='topic.description':
                    topic = lampadas.topics[uri.code]
                    newstring = topic.description[uri.lang]

                # Tables
                # 
                if token=='tablogin':
                    newstring = self.tablef.login(uri, build_user)
                if token=='tabdocs':
                    newstring = self.tablef.doctable(uri, build_user)
                if token=='tabeditdoc':
                    newstring = self.tablef.doc(uri)
                if token=='tabcvslog':
                    newstring = self.tablef.cvslog(uri)
                if token=='tabuser':
                    newstring = self.tablef.user(uri)
                if token=='tabmenus':
                    newstring = self.tablef.section_menus(uri, build_user)
                if token=='tabrecentnews':
                    newstring = self.tablef.recent_news(uri)
                if token=='tabtopics':
                    newstring = self.tablef.topics(uri)
                if token=='tabsubtopics':
                    newstring = self.tablef.subtopics(uri)
                if token=='tabsubtopic':
                    newstring = self.tablef.subtopic(uri)
                if token=='tabtypes':
                    newstring = self.tablef.types(uri)
                if token=='tabsessions':
                    newstring = self.tablef.sessions(uri, build_user)
                if token=='tablanguages':
                    newstring = self.tablef.languages(uri)
                if token=='tabtypedocs':
                    newstring = self.tablef.doctable(uri, build_user, type_code=uri.code)
                if token=='tabsubtopicdocs':
                    newstring = self.tablef.doctable(uri, build_user, subtopic_code=uri.code)
            
                # Blocks and Strings
                # 
                if newstring=='':
                    block = lampadasweb.blocks[token]
                    if block==None:
                        string = lampadasweb.strings[token]
                        if string==None:
                            log(1, 'Could not replace token ' + token)
                        else:
                            newstring = string.string[uri.lang]
                    else:
                        newstring = block.block
                
                # Add an error message if the token was not found
                # 
                if newstring=='':
                    log(1, 'Could not replace token ' + token)
                    newstring = 'ERROR (' + token + ')'
                
                html = html.replace(html[pos:pos2+1], newstring)
                html = html.replace('\|', 'DCM_PIPE')
                
                pos = html.find('|')
        
        html = html.replace('DCM_PIPE', '|')
    
        log(3, 'Page built ' + page.code)
        return html


page_factory = PageFactory()
combo_factory = ComboFactory()

def profile():
    import profile

    profile.run('page_factory.page("home")')
    
def main():
    if len(sys.argv[1:]):
        for arg in sys.argv[1:]:
            print page_factory.page(arg)
    else:
        profile()


if __name__=="__main__":
    main()
