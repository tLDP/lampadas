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

from Globals import *
from Config import config
from Log import log
from BaseClasses import *
from Languages import languages
from DataLayer import lampadas, Doc, User
from SourceFiles import sourcefiles
from ErrorTypes import errortypes
from Errors import errors
from WebLayer import lampadasweb, Page, NewsItem, String
from Widgets import widgets
from Sessions import sessions
from Lintadas import lintadas
from Stats import stats, Stat
from OMF import OMF
import os
import fpformat
import string

# FIXME: Replace the rest of the form elements, including buttons, with widgets in the widget library.

ICON_CELLS_COUNT = 4

# MimeType icons for downloadable formats. Not all are used yet.
ASCII_ICON_SM   = '<img src="|uri.base|themes/|theme|/images/ascii22x22.png"   alt="Text"   align="middle">'
ASCII_ICON      = '<img src="|uri.base|themes/|theme|/images/ascii32x32.png"   alt="Text"   align="middle">'
ASCII_ICON_BIG  = '<img src="|uri.base|themes/|theme|/images/ascii48x48.png"   alt="Text"   align="middle">'
CSS_ICON_SM     = '<img src="|uri.base|themes/|theme|/images/css22x22.png"     alt="CSS"    align="middle">'
CSS_ICON        = '<img src="|uri.base|themes/|theme|/images/css32x32.png"     alt="CSS"    align="middle">'
CSS_ICON_BIG    = '<img src="|uri.base|themes/|theme|/images/css48x48.png"     alt="CSS"    align="middle">'
EDIT_ICON_SM    = '<img src="|uri.base|themes/|theme|/images/edit22x22.png"    alt="Edit"   align="middle">'
EDIT_ICON       = '<img src="|uri.base|themes/|theme|/images/edit32x32.png"    alt="Edit"   align="middle">'
EDIT_ICON_BIG   = '<img src="|uri.base|themes/|theme|/images/edit48x48.png"    alt="Edit"   align="middle">'
FOLDER_ICON_SM  = '<img src="|uri.base|themes/|theme|/images/folder22x22.png"  alt="Folder" align="middle">'
FOLDER_ICON     = '<img src="|uri.base|themes/|theme|/images/folder32x32.png"  alt="Folder" align="middle">'
FOLDER_ICON_BIG = '<img src="|uri.base|themes/|theme|/images/folder48x48.png"  alt="Folder" align="middle">'
HTML_ICON_SM    = '<img src="|uri.base|themes/|theme|/images/html22x22.png"    alt="HTML"   align="middle">'
HTML_ICON       = '<img src="|uri.base|themes/|theme|/images/html32x32.png"    alt="HTML"   align="middle">'
HTML_ICON_BIG   = '<img src="|uri.base|themes/|theme|/images/html48x48.png"    alt="HTML"   align="middle">'
INFO_ICON_SM    = '<img src="|uri.base|themes/|theme|/images/info22x22.png"    alt="Info"   align="middle">'
INFO_ICON       = '<img src="|uri.base|themes/|theme|/images/info32x32.png"    alt="Info"   align="middle">'
INFO_ICON_BIG   = '<img src="|uri.base|themes/|theme|/images/info48x48.png"    alt="Info"   align="middle">'
LOG_ICON_SM     = '<img src="|uri.base|themes/|theme|/images/log22x22.png"     alt="Log"    align="middle">'
LOG_ICON        = '<img src="|uri.base|themes/|theme|/images/log32x32.png"     alt="Log"    align="middle">'
LOG_ICON_BIG    = '<img src="|uri.base|themes/|theme|/images/log48x48.png"     alt="Log"    align="middle">'
MULTI_ICON_SM   = '<img src="|uri.base|themes/|theme|/images/multi22x22.png"   alt="Multi"  align="middle">'
MULTI_ICON      = '<img src="|uri.base|themes/|theme|/images/multi32x32.png"   alt="Multi"  align="middle">'
MULTI_ICON_BIG  = '<img src="|uri.base|themes/|theme|/images/multi48x48.png"   alt="Multi"  align="middle">'
PDF_ICON_SM     = '<img src="|uri.base|themes/|theme|/images/pdf22x22.png"     alt="PDF"    align="middle">'
PDF_ICON        = '<img src="|uri.base|themes/|theme|/images/pdf32x32.png"     alt="PDF"    align="middle">'
PDF_ICON_BIG    = '<img src="|uri.base|themes/|theme|/images/pdf48x48.png"     alt="PDF"    align="middle">'
PS_ICON_SM      = '<img src="|uri.base|themes/|theme|/images/ps22x22.png"      alt="PS"     align="middle">'
PS_ICON         = '<img src="|uri.base|themes/|theme|/images/ps32x32.png"      alt="PS"     align="middle">'
PS_ICON_BIG     = '<img src="|uri.base|themes/|theme|/images/ps48x48.png"      alt="PS"     align="middle">'
TGZ_ICON_SM     = '<img src="|uri.base|themes/|theme|/images/tgz22x22.png"     alt="TGZ"    align="middle">'
TGZ_ICON        = '<img src="|uri.base|themes/|theme|/images/tgz32x32.png"     alt="TGZ"    align="middle">'
TGZ_ICON_BIG    = '<img src="|uri.base|themes/|theme|/images/tgz48x48.png"     alt="TGZ"    align="middle">'
UNK_ICON_SM     = '<img src="|uri.base|themes/|theme|/images/unknown22x22.png" alt="?"      align="middle">'
UNK_ICON        = '<img src="|uri.base|themes/|theme|/images/unknown32x32.png" alt="?"      align="middle">'
UNK_ICON_BIG    = '<img src="|uri.base|themes/|theme|/images/unknown48x48.png" alt="?"      align="middle">'
VIEW_ICON_SM    = 'View'
VIEW_ICON       = 'View'
VIEW_ICON_BIG   = 'View'


class Tables(LampadasCollection):

    def __init__(self):
        self.data = {}

    def bar_graph(self, value, max, lang):
        return str(value) + '/' + str(max)

    def viewdoc(self, uri):
        doc = lampadas.docs[uri.id]
        if doc==None:
            return '|blknotfound|'

        lintadas.check_doc(uri.id)
        metadata = doc.metadata()

        box = WOStringIO('<table class="box" width="100%%">' \
                         '<tr><th colspan="6">|strdocdetails|</th></tr>'
                         '<tr><td class="label">|strtitle|</td><td colspan="5">%s</td></tr>\n'
                         '<tr><td class="label">|strshort_desc|</td><td colspan="5">%s</td></tr>\n'
                         '<tr><td class="label">|strabstract|</td><td colspan="5">%s</td></tr>\n'
                         '<tr><td class="label">|strstatus|</td><td>%s</td>\n'
                         '    <td class="label">|strtype|</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strversion|</td><td>%s</td>\n'
                         '    <td class="label">|strshort_title|</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strwriting|</td><td>%s</td>\n'
                         '    <td class="label">|straccuracy|</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strpub_date|</td><td>%s</td>\n'
                         '    <td class="label">|strupdated|</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strlint_time|</td><td>%s</td>\n'
                         '    <td class="label">|strmirror_time|</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strpub_time|</td><td>%s</td>\n'
                         '    <td class="label">|strtickle_date|</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strmaintained|</td><td>%s</td>\n'
                         '    <td class="label">|strrating|</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strformat|</td><td>%s</td>\n'
                         '    <td class="label">|strdtd|</td><td>%s %s</td></tr>\n'
                         '<tr><td class="label">|strlanguage|</td><td>%s</td>\n'
                         '    <td class="label">|strmaint_wanted|</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strlicense|</td><td>%s %s</td>\n'
                         '    <td class="label">|strcopyright_holder|</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strtrans_master|</td><td colspan="3">%s</td></tr>\n'
                         '    <td class="label">|strreplacedby|</td><td colspan="3">%s</td></tr>\n'
                         '<tr><td class="label">|strisbn|</td><td>%s</td><td></td></tr>\n'
                         '</table>'
                         % (metadata.title,
                            doc.short_desc,
                            metadata.abstract,
                            widgets.pub_status_code(doc.pub_status_code, uri.lang, view=1),
                            widgets.type_code(doc.type_code, uri.lang, view=1),
                            metadata.version,
                            doc.short_title,
                            widgets.review_status_code(doc.review_status_code, uri.lang, view=1), 
                            widgets.tech_review_status_code(doc.tech_review_status_code, uri.lang, view=1),
                            metadata.pub_date, doc.last_update,
                            doc.lint_time, doc.mirror_time, doc.pub_time,
                            doc.tickle_date,
                            bool2yesno(doc.maintained),
                            self.bar_graph(doc.rating, 10, uri.lang),
                            widgets.format_code(metadata.format_code, uri.lang, view=1),
                            widgets.dtd_code(metadata.dtd_code, uri.lang, view=1),
                            metadata.dtd_version,
                            widgets.lang(doc.lang, uri.lang, view=1),
                            widgets.tf('maintainer_wanted', doc.maintainer_wanted, view=1),
                            widgets.license_code(doc.license_code, uri.lang, view=1),
                            doc.license_version,
                            doc.copyright_holder,
                            widgets.sk_seriesid(doc.sk_seriesid, view=1),
                            widgets.replaced_by_id(doc.replaced_by_id, view=1),
                            metadata.isbn
                            ))
        return box.get_value()

    def editdoc(self, uri):
        if (sessions.session==None or sessions.session.user.can_edit(doc_id=uri.id)==0):
            return '|blknopermission|'

        box = WOStringIO('<table class="box" width="100%">' \
                         '<tr><th colspan="6">|strdocdetails|</th></tr>')
                
        if uri.id > 0:
            lintadas.check_doc(uri.id)
            doc = lampadas.docs[uri.id]
            box.write('<form method=GET action="|uri.base|data/save/document" '\
                      'name="document">')
        else:

            # Create a new document
            doc = Doc()
            doc.lang = uri.lang
            doc.pub_status_code = 'P'
            doc.review_status_code = 'U'
            doc.tech_review_status_code = 'U'
            box.write('<form method=GET action="|uri.base|data/save/newdocument" '\
                      'name="document">')

        metadata = doc.metadata()

        # Set CSS class for defaulted data.
        format_code_class = ''
        dtd_code_class    = ''
        dtd_version_class = ''
        title_class       = ''
        abstract_class    = ''
        version_class     = ''
        pub_date_class    = ''
        isbn_class        = ''
        if doc.format_code=='' and metadata.format_code > '':
            format_code_class = ' class="defaulted"'
        if doc.dtd_code=='' and metadata.dtd_code > '':
            dtd_code_class = ' class="defaulted"'
        if doc.dtd_version=='' and metadata.dtd_version > '':
            dtd_version_class = ' class="defaulted"'
        if doc.title=='' and metadata.title > '':
            title_class = ' class="defaulted"'
        if doc.abstract=='' and metadata.abstract > '':
            abstract_class = ' class="defaulted"'
        if doc.version=='' and metadata.version > '':
            version_class = ' class="defaulted"'
        if doc.pub_date=='' and metadata.pub_date > '':
            pub_date_class = ' class="defaulted"'
        if doc.isbn=='' and metadata.isbn > '':
            isbn_class = ' class="defaulted"'
            
        box.write('<input name="username" type="hidden" value="%s">\n'
                  '<input name="doc_id" type="hidden" value="%s">\n'
                  '<tr><td class="label">|strtitle|</td><td colspan="5">%s</td></tr>\n'
                  '<tr><td class="label">|strshort_desc|</td><td colspan="5">%s</td></tr>\n'
                  '<tr><td class="label">|strabstract|</td><td colspan="5">%s</td></tr>\n'
                  '<tr><td class="label">|strstatus|</td><td>%s</td>\n'
                  '    <td class="label">|strtype|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strversion|</td><td>%s</td>\n'
                  '    <td class="label">|strshort_title|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strwriting|</td><td>%s</td>\n'
                  '    <td class="label">|straccuracy|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strpub_date|</td><td>%s</td>\n'
                  '    <td class="label">|strupdated|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strlint_time|</td><td>%s</td>\n'
                  '    <td class="label">|strmirror_time|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strpub_time|</td><td>%s</td>\n'
                  '    <td class="label">|strtickle_date|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strmaintained|</td><td>%s</td>\n'
                  '    <td class="label">|strrating|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strformat|</td><td>%s</td>\n'
                  '    <td class="label">|strdtd|</td><td>%s %s</td></tr>\n'
                  '<tr><td class="label">|strlanguage|</td><td>%s</td>\n'
                  '    <td class="label">|strmaint_wanted|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strlicense|</td><td>%s %s</td>\n'
                  '    <td class="label">|strcopyright_holder|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strtrans_master|</td><td colspan="3">%s</td></tr>\n'
                  '    <td class="label">|strreplacedby|</td><td colspan="3">%s</td></tr>\n'
                  '<tr><td class="label">|strisbn|</td><td>%s</td><td></td></tr>\n'
                  '<tr><td></td><td>%s</td></tr>'
                  '</table></form>'
                  % (sessions.session.username, doc.id,
                     widgets.title(metadata.title, css_class=title_class),
                     widgets.short_desc(doc.short_desc),
                     widgets.abstract(metadata.abstract, css_class=abstract_class),
                     widgets.pub_status_code(doc.pub_status_code, uri.lang),
                     widgets.type_code(doc.type_code, uri.lang),
                     widgets.version(metadata.version, css_class=version_class),
                     widgets.short_title(doc.short_title),
                     widgets.review_status_code(doc.review_status_code, uri.lang), 
                     widgets.tech_review_status_code(doc.tech_review_status_code, uri.lang),
                     widgets.pub_date(metadata.pub_date, css_class=pub_date_class), widgets.last_update(doc.last_update),
                     widgets.lint_time(doc.lint_time), widgets.mirror_time(doc.mirror_time), widgets.pub_time(doc.pub_time),
                     widgets.tickle_date(doc.tickle_date),
                     bool2yesno(doc.maintained),
                     self.bar_graph(doc.rating, 10, uri.lang),
                     widgets.format_code(metadata.format_code, uri.lang, css_class=format_code_class),
                     widgets.dtd_code(metadata.dtd_code, uri.lang, css_class=dtd_code_class),
                     widgets.dtd_version(metadata.dtd_version, uri.lang, css_class=dtd_version_class),
                     widgets.lang(doc.lang, uri.lang),
                     widgets.tf('maintainer_wanted', doc.maintainer_wanted),
                     widgets.license_code(doc.license_code, uri.lang),
                     widgets.license_version(doc.license_version),
                     widgets.copyright_holder(doc.copyright_holder),
                     widgets.sk_seriesid(doc.sk_seriesid),
                     widgets.replaced_by_id(doc.replaced_by_id),
                     widgets.isbn(metadata.isbn, css_class=isbn_class),
                     widgets.save()))
        return box.get_value()

    def viewdocversions(self, uri):
        doc = lampadas.docs[uri.id]
        if doc==None:
            return '|blknotfound|'

        log(3, 'Creating viewdocversions table')
        doc = lampadas.docs[uri.id]
        metadata = doc.metadata()
        box = WOStringIO('<table class="box" width="100%">\n'
                         '<tr><th colspan="4">|strdocversions|</th></tr>\n'
                         '<tr><th class="collabel">|strversion|</th>\n'
                         '    <th class="collabel">|strdate|</th>\n'
                         '    <th class="collabel">|strinitials|</th>\n'
                         '    <th class="collabel">|strcomments|</th></tr>\n')
        odd_even = OddEven()
        keys = doc.versions.sort_by('pub_date')
        for key in keys:
            version = doc.versions[key]
            box.write('<tr class="%s"><td>%s</td><td>%s</td><td>%s</td><td style="width:100%%">%s</td></tr>\n'
                      % (odd_even.get_next(), version.version, version.pub_date, version.initials, version.notes))
        box.write('</table>')
        return box.get_value()
        
    def editdocversions(self, uri):
        if (sessions.session==None or sessions.session.user.can_edit(doc_id=uri.id)==0):
            return '|blknopermission|'

        log(3, 'Creating editdocversions table')
        doc = lampadas.docs[uri.id]
        metadata = doc.metadata()
        box = WOStringIO('<table class="box" width="100%">\n'
                         '<tr><th colspan="6">|strdocversions|</th></tr>\n'
                         '<tr><th class="collabel">|strversion|</th>\n'
                         '    <th class="collabel">|strdate|</th>\n'
                         '    <th class="collabel">|strinitials|</th>\n'
                         '    <th class="collabel">|strcomments|</th>\n'
                         '    <th class="collabel" colspan="2">|straction|</th></tr>')
        odd_even = OddEven()
        keys = doc.versions.sort_by('pub_date')
        for key in keys:
            version = doc.versions[key]
            box.write('<form method=GET action="|uri.base|data/save/document_version" name="document_version">'
                      '<input name="rev_id" type=hidden value="%s">\n'
                      '<input name="doc_id" type=hidden value="%s">\n'
                      '<tr class="%s"><td>%s</td><td>%s</td><td>%s</td><td style="width:100%%">%s</td><td>%s|strdelete|</td><td>%s</td></tr>\n'
                      '</form>\n'
                      % (version.id,
                      version.doc_id,
                      odd_even.get_next(),
                      widgets.version(version.version),
                      widgets.pub_date(version.pub_date),
                      widgets.initials(version.initials),
                      widgets.notes(version.notes),
                      widgets.delete(),
                      widgets.save()))
        box.write('<form method=GET action="|uri.base|data/save/newdocument_version" name="document_version">'
                  '<input name="doc_id" type=hidden value="%s">\n'
                  '<tr class="%s"><td>%s</td><td>%s</td><td>%s</td><td style="width:100%%">%s</td><td></td><td>%s</td></tr>'
                  '</form></table>'
                  % (doc.id, odd_even.get_next(), widgets.version(''), widgets.pub_date(''), widgets.initials(''), widgets.notes(''), widgets.add()))
        return box.get_value()

    def viewdocfiles(self, uri):
        doc = lampadas.docs[uri.id]
        if doc==None:
            return '|blknotfound|'

        log(3, 'Creating viewdocfiles table')
        box = WOStringIO('<table class="box" width="100%%">'
                         '<tr><th colspan="6">%s</th></tr>'
                         % ('|strdocfiles|'))
        keys = doc.files.sort_by('filename')
        for key in keys:
            lintadas.check_file(key)
            docfile = doc.files[key]
            sourcefile = sourcefiles[key]
            if sourcefile.errors.count() > 0:
                css_class = ' error'
            else:
                css_class = ''
            box.write('<tr><td class="sectionlabel%s" colspan="6"><a href="%ssourcefile/%s%s">%s</a></td></tr>\n'
                      '<tr><td class="label">|strprimary|</td><td>%s</td>\n'
                      '    <td class="label">|strfilesize|</td><td>%s</td>\n'
                      '    <td class="label">|strupdated|</td><td>%s</td></tr>\n'
                      '<tr><td class="label">|strformat|</td><td>%s</td>\n'
                      '    <td class="label">|strdtd|</td><td>%s</td>\n'
                      '    <td class="label">|strfilemode|</td><td>%s</td></tr>\n'
                      % (css_class, uri.base, docfile.filename, uri.lang_ext,
                         widgets.filename_compressed(sourcefile.filename),
                         widgets.tf('top', docfile.top, view=1), sourcefile.filesize, sourcefile.updated,
                         widgets.format_code(sourcefile.format_code, uri.lang, view=1),
                         widgets.dtd_code(sourcefile.dtd_code, uri.lang, view=1),
                         widgets.filemode(sourcefile.filemode)))
        box.write('</table>')
        return box.get_value()

    def editdocfiles(self, uri):
        if (sessions.session==None or sessions.session.user.can_edit(doc_id=uri.id)==0):
            return '|blknopermission|'

        log(3, 'Creating editdocfiles table')
        box = WOStringIO('<table class="box" width="100%%">'
                         '<tr><th colspan="6">%s</th></tr>'
                         % ('|strdocfiles|'))
        doc = lampadas.docs[uri.id]
        keys = doc.files.sort_by('filename')
        for key in keys:
            lintadas.check_file(key)
            docfile = doc.files[key]
            sourcefile = sourcefiles[key]
            if sourcefile.errors.count() > 0:
                css_class = ' error'
            else:
                css_class = ''
            box.write('<form method=GET action="|uri.base|data/save/document_file" name="document_file">' \
                      '<input type=hidden name="doc_id" value="%s">\n' \
                      '<input type=hidden name="filename" value="%s">\n' \
                      '<tr><td class="sectionlabel%s" colspan="6"><a href="%ssourcefile/%s%s">%s</a></td></tr>\n' \
                      '<tr><td class="label">|strprimary|</td><td>%s</td>\n' \
                      '    <td class="label">|strfilesize|</td><td>%s</td>\n' \
                      '    <td class="label">|strupdated|</td><td>%s</td></tr>\n'
                      '<tr><td class="label">|strformat|</td><td>%s</td>\n' \
                      '    <td class="label">|strdtd|</td><td>%s</td>\n' \
                      '    <td class="label">|strfilemode|</td><td>%s</td></tr>\n' \
                      '<tr><td colspan="5"></td><td><input type="checkbox" name="delete">|strdelete|<input type="submit" name="action" value="|strsave|"></td></tr>\n' \
                      '</form>'
                      % (doc.id, docfile.filename, css_class, uri.base, docfile.filename, uri.lang_ext,
                         widgets.filename_compressed(sourcefile.filename),
                         widgets.tf('top', docfile.top), sourcefile.filesize, sourcefile.updated,
                         widgets.format_code(sourcefile.format_code, uri.lang, view=1),
                         widgets.dtd_code(sourcefile.dtd_code, uri.lang, view=1),
                         widgets.filemode(sourcefile.filemode)))
        
        # Add a new docfile
        box.write('<tr><form method=GET action="|uri.base|data/save/newdocument_file" name="document_file">\n'
                  '<input name="doc_id" type="hidden" value="%s">\n'
                  '<td colspan="6"><input type="text" name="filename" size="30" style="width:100%%"></td></tr>\n'
                  '<tr><td class="label">|strprimary|</td><td colspan="5">%s</td>\n'
                  '<td><input type="submit" name="action" value="|stradd|"></td></tr>\n'
                  '</form>\n'
                  '</table>\n'
                  % (doc.id, widgets.tf('top', (doc.files.count()==0))))
        return box.get_value()
        
    def viewdocusers(self, uri):
        doc = lampadas.docs[uri.id]
        if doc==None:
            return '|blknotfound|'

        log(3, 'Creating viewdocusers table')
        box = WOStringIO('<table class="box" width="100%">'
                         '<tr><th colspan="4">|strdocusers|</th></tr>'
                         '<tr><th class="collabel">|strusername|</th>'
                         '    <th class="collabel">|stractive|</th>'
                         '    <th class="collabel">|strrole|</th>'
                         '    <th class="collabel">|stremail|</th></tr>')
        keys = doc.users.sort_by('username')
        odd_even = OddEven()
        for key in keys:
            docuser = doc.users[key]
            box.write('<tr class="%s"><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n'
                      % (odd_even.get_next(),
                         docuser.username,
                         widgets.tf('active', docuser.active, view=1),
                         widgets.role_code(docuser.role_code, uri.lang, view=1),
                         docuser.email))

        box.write('</table>\n')
        return box.get_value()
        
    def editdocusers(self, uri):
        if (sessions.session==None or sessions.session.user.can_edit(doc_id=uri.id)==0):
            return '|blknopermission|'

        log(3, 'Creating editdocusers table')
        doc = lampadas.docs[uri.id]
        box = WOStringIO('<table class="box" width="100%">'
                         '<tr><th colspan="6">|strdocusers|</th></tr>'
                         '<tr><th class="collabel">|strusername|</th>'
                         '    <th class="collabel">|stractive|</th>'
                         '    <th class="collabel">|strrole|</th>'
                         '    <th class="collabel">|stremail|</th>'
                         '    <th class="collabel" colspan="2">|straction|</th></tr>')
        keys = doc.users.sort_by('username')
        odd_even = OddEven()
        for key in keys:
            docuser = doc.users[key]
            box.write('<form method=GET action="|uri.base|data/save/document_user" name="document_user">'
                      '<input type=hidden name="doc_id" value="%s">\n'
                      '<input type=hidden name="username" value="%s">\n'
                      '<tr class="%s">\n'
                      % (doc.id, docuser.username, odd_even.get_next()))
            if sessions.session:
                if sessions.session.user.admin==1 or sessions.session.user.sysadmin==1:
                    box.write('<td><a href="|uri.base|user/%s">%s</a></td>\n'
                              % (docuser.username, docuser.username))
                else:
                    box.write('<td>%s</td>\n' % docuser.username)
            else:
                box.write('<td>%s</td>\n' % docuser.username)
            box.write('<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n'
                      '</form>\n'
                      % (widgets.tf('active', docuser.active),
                         widgets.role_code(docuser.role_code, uri.lang),
                         widgets.email(docuser.email),
                         widgets.delete(),
                         widgets.save()))

        box.write('<form method=GET action="|uri.base|data/save/newdocument_user" name="document_user">'
                  '<input name="doc_id" type=hidden value="%s">\n'
                  '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td></td><td>%s</td></tr>\n'
                  '</form></table>\n'
                  % (doc.id,
                  widgets.username(''),
                  widgets.tf('active', 1),
                  widgets.role_code('', uri.lang),
                  widgets.email(''),
                  widgets.add()))
        return box.get_value()
        
    def viewdoctopics(self, uri):
        doc = lampadas.docs[uri.id]
        if doc==None:
            return '|blknotfound|'

        log(3, 'Creating viewdoctopics table')
        doc = lampadas.docs[uri.id]
        box = WOStringIO('<table class="box" width="100%">'
                         '<tr><th>|strdoctopics|</th></tr>\n'
                         '<tr><th class="collabel">|strtopic|</th></tr>\n')
        doc = lampadas.docs[uri.id]
        topic_codes = lampadas.topics.sort_by('sort_order')
        odd_even = OddEven()
        for topic_code in topic_codes:
            doctopic = doc.topics[topic_code]
            if doctopic:
                topic = lampadas.topics[topic_code]
                box.write('<tr class="%s"><td><a href="|uri.base|topic/%s|uri.lang_ext|">%s</a></td></tr>'
                          % (odd_even.get_next(), topic_code, topic.title[uri.lang]))
        box.write('</table>')
        return box.get_value()

    def editdoctopics(self, uri):
        if (sessions.session==None or sessions.session.user.can_edit(doc_id=uri.id)==0):
            return '|blknopermission|'

        log(3, 'Creating editdoctopics table')
        doc = lampadas.docs[uri.id]
        box = WOStringIO('<table class="box" width="100%">'
                         '<tr><th colspan="2">|strdoctopics|</th></tr>\n'
                         '<tr><th class="collabel">|strtopic|</th>\n'
                         '    <th class="collabel">|straction|</th></tr>\n')
        doc = lampadas.docs[uri.id]
        topic_codes = lampadas.topics.sort_by('sort_order')
        odd_even = OddEven()
        for topic_code in topic_codes:
            doctopic = doc.topics[topic_code]
            if doctopic:
                topic = lampadas.topics[topic_code]
                box.write('<form method=GET action="|uri.base|data/save/deldocument_topic" name="document_topic">\n'
                          '<input type=hidden name="doc_id" value="%s">\n'
                          '<input type=hidden name="topic_code" value="%s">\n'
                          '<tr class="%s"><td><a href="|uri.base|topic/%s|uri.lang_ext|">%s</a></td>'
                          '               <td><input type=submit name="action" value="|strdelete|"></td></tr>\n'
                          '</form>\n'
                          % (doc.id, topic_code, odd_even.get_next(), topic_code, topic.title[uri.lang]))
        box.write('<form method=GET action="|uri.base|data/save/newdocument_topic" name="document_topic">\n'
                  '<input name="doc_id" type=hidden value="%s">\n'
                  '<tr><td>%s</td><td>%s</td></tr>'
                  '</form></table>\n'
                  % (doc.id,
                     widgets.topic_code('', uri.lang),
                     widgets.add()))
        return box.get_value()

    def viewdocnotes(self, uri):
        doc = lampadas.docs[uri.id]
        if doc==None:
            return '|blknotfound|'

        log(3, 'Creating viewdocnotes table')
        box = WOStringIO('<table class="box" width="100%">'
                         '<tr><th colspan="3">|strdocnotes|</th></tr>\n'
                         '<tr><th class="collabel">|strdate_time|</th>\n'
                         '    <th class="collabel">|strusername|</th>\n'
                         '    <th class="collabel">|strcomments|</th></tr>\n')
        note_ids = doc.notes.sort_by('created')
        odd_even = OddEven()
        for note_id in note_ids:
            note = doc.notes[note_id]
            box.write('<tr class="%s"><td>%s</td><td>%s</td><td>%s</td></tr>\n'
                      % (odd_even.get_next(), note.created, note.creator, note.notes))
        box.write('</table>\n')
        return box.get_value()

    def editdocnotes(self, uri):
        if (sessions.session==None or sessions.session.user.can_edit(doc_id=uri.id)==0):
            return '|blknopermission|'

        log(3, 'Creating editdocnotes table')
        doc = lampadas.docs[uri.id]
        box = WOStringIO('<table class="box" width="100%">'
                         '<tr><th colspan="4">|strdocnotes|</th></tr>\n'
                         '<tr><th class="collabel">|strdate_time|</th>\n'
                         '    <th class="collabel">|strusername|</th>\n'
                         '    <th class="collabel">|strcomments|</th>\n'
                         '    <th class="collabel">|straction|</th></tr>\n')
        note_ids = doc.notes.sort_by('created')
        odd_even = OddEven()
        for note_id in note_ids:
            note = doc.notes[note_id]
            box.write('<tr class="%s"><td>%s</td><td>%s</td><td>%s</td><td></td></tr>\n'
                      % (odd_even.get_next(), note.created, note.creator, note.notes))
        box.write('<form method=GET action="|uri.base|data/save/newdocument_note" name="document_note">'
                  '<input name="doc_id" type=hidden value="%s">\n'
                  '<input name="creator" type=hidden value="%s">\n'
                  '<tr><td></td><td></td>\n'
                  '<td>%s</td>\n'
                  '<td>%s</td></tr>\n'
                  '</form></table>\n'
                  % (doc.id, sessions.session.username,
                     widgets.notes(''), widgets.add()))
        return box.get_value()

    def doctranslations(self, uri):
        """
        Builds a table of all available translations of a document.
        Based on the DocTable.
        """
        
        doc = lampadas.docs[uri.id]
        if doc==None:
            return '|blknotfound|'

        log(3, 'Creating doctranslations table')
        return self.doctable(uri, sk_seriesid=doc.sk_seriesid,
                             columns={'|strlanguage|':  'lang',
                                      '|strversion|':   'version',
                                      '|strupdated|':   'last_update',
                                      '|strpub_date|':  'pub_date',
                                     },
                             show_search=0)

    def errors(self, uri):
        """
        Builds a complete list of all errors reported by Lintadas.
        It uses docerrors() and docfileerrors(), and just concatenates
        all of their contents.
        """

        if not sessions.session:
            return '|blknopermission|'

        log(3, 'Creating errors table')
        doc_ids = lampadas.docs.sort_by('title')
        box = WOStringIO('')
        for doc_id in doc_ids:
            doc = lampadas.docs[doc_id]
            metadata = doc.metadata()

            # Only display docs the user has rights to.
            if sessions.session.user.can_edit(doc_id=doc_id)==0:
                continue
            if doc.lang==uri.lang:
                uri.id = doc_id
                doctable = self.docerrors(uri)
                filestable = self.docfileerrors(uri)
                if doctable > '' or filestable > '':
                    box.write('<h1><a href="|uri.base|document_main/%s|uri.lang_ext|">%s</a>%s</h1>'
                              % (str(doc.id), EDIT_ICON, metadata.title))
                if doctable > '':
                    box.write('<p>' + doctable)
                if filestable > '':
                    box.write('<p>' + filestable)
        return box.get_value()

    def docerrors(self, uri):
        doc = lampadas.docs[uri.id]
        if doc==None:
            return '|blknotfound|'

        if doc.errors.count()==0:
            return ''

        log(3, 'Creating docerrors table')
        box = WOStringIO('<table class="box" width="100%">'
                        '<tr><th colspan="4">|strdocerrs|</th></tr>\n'
                        '<tr><th class="collabel">|strtimestamp|</th>\n'
                        '    <th class="collabel">|strid|</th>\n'
                        '    <th class="collabel">|strtype|</th>\n'
                        '    <th class="collabel">|strerror|</th></tr>\n')
        err_ids = doc.errors.sort_by('created')
        odd_even = OddEven()
        for err_id in err_ids:
            docerror = doc.errors[err_id]
            error = errors[err_id]
            errtype = errortypes[error.err_type_code]
            box.write('<tr class="%s"><td>%s</td><td>%s</td><td>%s</td><td>%s<br><pre>%s</pre></td></tr>'
                      % (odd_even.get_next(),
                         docerror.created,
                         docerror.err_id,
                         errtype.name[uri.lang],
                         error.name[uri.lang],
                         html_encode(docerror.notes)))
        box.write('</table>\n')
        return box.get_value()

    def docfileerrors(self, uri):
        doc = lampadas.docs[uri.id]
        if doc==None:
            return '|blknotfound|'

        if doc.files.error_count==0:
            return ''

        log(3, 'Creating docfileerrors table')
        box = WOStringIO('<table class="box" width="100%">\n'
                         '<tr>\n<th colspan="3">|strfileerrs|</th>\n</tr>\n'
                         '<tr>\n<th class="collabel">|strid|</th>\n'
                         '<th class="collabel">|strerror|</th>\n'
                         '<th class="collabel">|strfilename|</th>\n</tr>\n')
        filenames = doc.files.sort_by('filename')
        odd_even = OddEven()
        for filename in filenames:
            sourcefile = sourcefiles[filename]
            err_ids = sourcefile.errors.sort_by('created')
            for err_id in err_ids:
                fileerror = sourcefile.errors[err_id]
                error = errors[err_id]
                box.write('<tr class="%s">\n<td>%s</td>\n<td>%s</td>\n<td><a href="|uri.base|sourcefile/%s">%s</a></td>\n</tr>\n'
                          % (odd_even.get_next(), fileerror.err_id, error.name[uri.lang],
                             sourcefile.filename, widgets.filename_compressed(sourcefile.filename)))
        box.write('</table>\n')
        return box.get_value()

    def filereports(self, uri):
        if not sessions.session:
            return '|blknopermission|'
        elif sessions.session.user.can_edit(doc_id=uri.id)==0:
            return '|blknopermission|'

        log(3, 'Creating filereports table')
        sourcefile = sourcefiles[uri.filename]
        display_filename = widgets.filename_compressed(sourcefile.filename)

        box = WOStringIO('<table class="box" width="100%%">'
                         '<tr><th colspan="2">|strfilereports|</th></tr>\n'
                         '<tr><th colspan="2" class="sectionlabel">%s</th></tr>\n'
                         % display_filename)
        report_codes = lampadasweb.file_reports.sort_by_lang('name', uri.lang)
        odd_even = OddEven()
        for report_code in report_codes:
            report = lampadasweb.file_reports[report_code]
            if report.only_cvs==0 or sourcefile.in_cvs==1:
                box.write('<tr class="%s"><td><a href="|uri.base|file_report/%s/%s%s">%s</a></td><td>%s</td></tr>\n'
                % (odd_even.get_next, report.code, uri.filename, uri.lang_ext, report.name[uri.lang], report.description[uri.lang]))
        box.write('</table>\n')
        return box.get_value()

    def filereport(self, uri):
        if not sessions.session:
            return '|blknopermission|'
        elif sessions.session.user.can_edit(doc_id=uri.id)==0:
            return '|blknopermission|'

        log(3, 'Creating filereport table')

        # Build and execute the command
        report = lampadasweb.file_reports[uri.code]
        command = report.command
        sourcefile = sourcefiles[uri.filename]

        # Write local filename in case script wants it.
        fh = open('/tmp/lampadas_localname.txt', 'w')
        fh.write(sourcefile.localname + '\n')
        fh.close()
        
        # Write CVS-relative filename in case script wants it.
        fh = open('/tmp/lampadas_filename.txt', 'w')
        fh.write(sourcefile.filename + '\n')
        fh.close()
        
        child_stdin, child_stdout, child_stderr  = os.popen3(command)
        stdout = child_stdout.read()
        stderr = child_stderr.read()
        child_stdin.close()
        child_stdout.close()
        child_stderr.close()

        box = WOStringIO('<table class="box" width="100%%">'
                         '<tr><th>%s</th></tr>\n'
                         '<tr><th class="collabel">|stroutput|</th></tr>\n'
                         '<tr class="odd"><td><pre>%s</pre></td></tr>\n'
                         '<tr><th class="collabel">|strerrors|</th></tr>\n'
                         '<tr class="odd"><td><pre>%s</pre></td></tr>\n'
                         % (report.name[uri.lang], stdout, stderr))
        if sessions.session:
            if sessions.session.user.admin==1 or sessions.session.user.sysadmin==1:
                box.write('<tr><th class="collabel">|strcommand|</th></tr>\n'
                          '<tr class="odd"><td><pre>%s</pre></td></tr>\n'
                          % command)
        box.write('</table>\n')
        return box.get_value()

    def letters(self, uri):
        log(3, 'Creating letter table')
        box = WOStringIO('<table class="tab"><tr>\n')
        for letter in string.uppercase:
            if letter==uri.letter:
                box.write('<th class="selected_tab">%s</th>\n' % letter)
            else:
                box.write('<th><a href="|uri.base|%s/%s|uri.lang_ext|">%s</a></th>\n'
                % (uri.page_code, letter, letter))
        box.write('</tr></table>\n')
        return box.get_value()
        
    def users(self, uri):
        if not sessions.session:
            return '|tabnopermission|'
        elif sessions.session.user.admin==0 and sessions.session.user.sysadmin==0:
            return '|tabnopermission|'
        elif uri.letter=='':
            return ''
            
        log(3, 'Creating users table')
        box = WOStringIO('<table class="box" width="100%%"><tr><th colspan="3">|strusers|</th></tr>\n'
                         '<tr><th class="collabel" colspan="2">|strusername|</th>\n'
                         '    <th class="collabel">|strname|</th></tr>\n')
        if uri.letter > '':
            usernames = lampadas.users.letter_keys(uri.letter)
            odd_even = OddEven()
            for username in usernames:
                user = lampadas.users[username]
                box.write('<tr class="%s"><td><a href="|uri.base|user/%s|uri.lang_ext|">%s</a></td><td>%s</td><td>%s</a></td></tr>\n'
                          % (odd_even.get_next(), username, EDIT_ICON_SM, username, user.name))
        box.write('</table>\n')
        return box.get_value()

    def user(self, uri):
        if sessions.session==None:
            return '|blknopermission|'
        elif sessions.session.user.can_edit(username=uri.username)==0:
            return '|blknopermission|'

        if uri.username > '':
            user = lampadas.users[uri.username]
            if user==None:
                return '|blknotfound|'
            box = WOStringIO('<form method=GET action="|uri.base|data/save/user" name="user">\n')
        else:
            user = User()
            box = WOStringIO('<form method=GET action="/data/save/newuser" name="user">\n')
        box.write('<table class="box" width="100%">\n'
                  '<tr><th colspan="2">|struserdetails|</th></tr>\n'
                  '<tr><td class="label">|strusername|</td>')
        if user.username=='':
            box.write('<td><input type="text" name="username"></td></tr>\n')
        else:
            box.write('<td><input name="username" type=hidden value="%s">%s</td></tr>\n'
                      % (user.username, user.username))
        box.write('<tr><td class="label">|strfirst_name|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strmiddle_name|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|strsurname|</td><td>%s</td></tr>\n'
                  '<tr><td class="label">|stremail|</td><td>%s</td></tr>\n'
                  % (widgets.first_name(user.first_name),
                     widgets.middle_name(user.middle_name),
                     widgets.surname(user.surname),
                     widgets.email(user.email)))

        if user.username=='':
            box.write('<tr><td class="label">|strpassword|</td><td>%s</td></tr>\n'
                      % widgets.newpassword())
        else:
            if sessions.session:
                if sessions.session.user.admin==1 or sessions.session.user.sysadmin==1:
                    box.write('<tr><td class="label">|strpassword|</td><td>%s</td></tr>\n' % user.password)
            box.write('<tr><td class="label">|strnewpassword|</td><td>%s</td></tr>\n' % widgets.newpassword())
        if sessions.session.user and (sessions.session.user.admin > 0 or sessions.session.user.sysadmin > 0):
            box.write('<tr><td class="label">|stradmin|</td><td>%s</td></tr>\n' % widgets.tf('admin', user.admin))
        else:
            box.write('<input name="admin" type="hidden" value="%s">\n'
                      '<tr><td class="label">|stradmin|</td><td>%s</td></tr>\n'
                      % (user.admin, bool2yesno(user.admin)))
        if sessions.session.user and sessions.session.user.sysadmin > 0:
            box.write('<tr><td class="label">|strsysadmin|</td><td>%s</td></tr>\n' % widgets.tf('sysadmin', user.sysadmin))
        else:
            box.write('<input name="sysadmin" type="hidden" value="%s">\n'
                      '<tr><td class="label">|strsysadmin|</td><td>%s</td></tr>\n'
                      % (user.sysadmin, bool2yesno(user.sysadmin)))
        box.write('<tr><td class="label">|strcomments|</td><td style="width:100%%">%s</td></tr>\n'
                  '<tr><td></td><td>%s</td></tr>\n'
                  '</table></form>\n'
                  % (widgets.notes(user.notes), widgets.save()))
        return box.get_value()
        
    def doctable(self, uri,
                 title='',
                 short_title='',
                 pub_status_code='',
                 type_code='',
                 topic_code='',
                 username='',
                 maintained='',
                 maintainer_wanted='',
                 lang='',
                 review_status_code='',
                 tech_review_status_code='',
                 pub_date='',
                 last_update='',
                 tickle_date='',
                 isbn='',
                 rating='',
                 format_code='',
                 dtd_code='',
                 license_code='',
                 copyright_holder='',
                 sk_seriesid='',
                 abstract='',
                 short_desc='',
                 collection_code='',
                 columns={},
                 layout='compact',
                 show_search=0
                ):
        """
        Creates a listing of all documents which fit the parameters passed in.

        You can select a layout from "compact" or "expanded". Compact is one line
        per document; expanded is a table per document. The expanded layout does
        not accept additional columns to be requested, and ignores the columns{}
        parameter.

        The DocTable includes its own search form, although the search form
        can also stand alone.
        """

        log(3, "Creating doctable")

        # Table header for compact layout
        if layout=='compact':
            colspan = ICON_CELLS_COUNT + len(columns) + 1
            box = WOStringIO('<table class="box" width="100%%"><tr><th colspan="%s">|strdoctable|</th></tr>\n'
                             '<tr><th class="collabel" colspan="%s" align="center">|strtitle|</th>'
                             % (colspan, ICON_CELLS_COUNT + 1))
            for column in columns.keys():
                box.write('<th class="collabel">%s</td>' % column)
            box.write('</tr>\n')
        elif layout=='expanded':
            box = WOStringIO('')

        keys = lampadas.docs.sort_by("title")
        odd_even = OddEven()
        for key in keys:
            doc = lampadas.docs[key]
            metadata = doc.metadata()

            # Don't include unpublished documents
            # except for admins and owners, unless config says otherwise
            if doc.pub_time=='':
                if sessions.session==None:
                    if config.world_can_see_unpublished==0:
                        continue

            # Filter documents according to parameters passed in
            # by the calling routine.
            if username > '':
                if doc.users[username]==None:
                    continue
            if lang > '':
                if doc.lang <> lang:
                    continue
            if pub_status_code > '':
                if doc.pub_status_code <> pub_status_code:
                    continue
            
            # If any other parameters were specified, limit the documents
            # to those which match the requirements.
            if type_code > '':
                if doc.type_code <> type_code:
                    continue
            if topic_code > '':
                topic = lampadas.topics[topic_code]
                if topic.docs[doc.id]==None:
                    continue
            if maintained > '':
                if doc.maintained <> int(maintained):
                    continue
            if maintainer_wanted > '':
                if doc.maintainer_wanted <> int(maintainer_wanted):
                    continue
            if title > '':
                if metadata.title.upper().find(title.upper())==-1:
                    continue
            if short_desc > '':
                if doc.short_title.upper().find(short_title.upper())==-1:
                    continue
            if review_status_code > '':
                if doc.review_status_code <> review_status_code:
                    continue
            if review_status_code > '':
                if doc.review_status_code <> review_status_code:
                    continue
            if tech_review_status_code > '':
                if doc.tech_review_status_code <> tech_review_status_code:
                    continue
            if pub_date > '':
                if metadata.pub_date <> pub_date:
                    continue
            if last_update > '':
                if doc.last_update <> last_update:
                    continue
            if tickle_date > '':
                if doc.tickle_date <> tickle_date:
                    continue
            if isbn > '':
                if metadata.isbn <> isbn:
                    continue
            if rating > '':
                if doc.rating <> int(rating):
                    continue
            if format_code > '':
                if doc.format_code <> format_code:
                    continue
            if dtd_code > '':
                if metadata.dtd_code <> dtd_code:
                    continue
            if license_code > '':
                if doc.license_code <> license_code:
                    continue
            if copyright_holder > '':
                if doc.copyright_holder.upper().find(copyright_holder.upper())==-1:
                    continue
            if sk_seriesid > '':
                if doc.sk_seriesid.find(sk_seriesid)==-1:
                    continue
            if abstract > '':
                if metadata.abstract.upper().find(abstract.upper())==-1:
                    continue
            if short_desc > '':
                if doc.short_desc.upper().find(short_desc.upper())==-1:
                    continue
            if collection_code > '':
                if collection_code not in doc.collections.keys():
                    continue

            # Doc passed all filters, so include it in the table.
            if layout=='compact':
                box.write('<tr class="%s">\n' % odd_even.get_next())
               
                box.write(self.document_icon_cells(doc.id, 'td'))

                # Format the title differently to flag its status
                display_title = html_encode(widgets.title_compressed(metadata.title))

                if doc.pub_time > '':
                    box.write('<td style="width:100%%"><a href="|uri.base|doc/%s/index.html">%s</a></td>\n'
                              % (str(doc.id), display_title))
                elif doc.errors.count() > 0 or doc.files.error_count > 0:
                    box.write('<td style="width:100%%" class="error">%s</td>\n' % display_title)
                else:
                    box.write('<td style="width:100%%">%s</td>\n' % display_title)

                # Now any custom columns.
                for column in columns.keys():
                    box.write('<td>%s</td>\n' % getattr(doc, columns[column]))
                box.write('</tr>\n')

            # This is a blocky extended listing, complete with abstracts.
            elif layout=='expanded':

                # Link to the online output.
                if doc.pub_time > '':
                    block_indexlink = '<td width=32><a href="|uri.base|doc/' + str(doc.id) + '/index.html">' + HTML_ICON + '</a></td>'
                else:
                    block_indexlink = '<td width=32></td>'
                
                # Folder icon
                if doc.pub_time > '':
                    block_dllink = '<td width=32><a href="|uri.base|docdownloads/' + str(doc.id) + '/">' + FOLDER_ICON + '</a></td>'
                else:
                    block_dllink = ('<td width=32></td>')

                # Edit icon
                block_editlink = '<td width=32><a href="|uri.base|document_main/' + str(doc.id) + '|uri.lang_ext|">' + EDIT_ICON + '</a></td>'

                # Format the title based on the presence of errors.
                if doc.errors.count() > 0 or doc.files.error_count > 0:
                    block_title = '<th colspan="4" class="error">' + html_encode(widgets.title_compressed(metadata.title)) + '</th>'
                else:
                    block_title = '<th colspan="4">' + html_encode(widgets.title_compressed(metadata.title)) + '</th>'

                # Finally, pull in the abstract.
                block_abstract = '<td>' + html_encode(metadata.abstract) + '</td>'

                box.write('<table class="box nontabular" width="100%%">\n' \
                          '  <tr>%s</tr>\n' \
                          '  <tr>%s\n' \
                          '      %s\n' \
                          '      %s\n' \
                          '      %s\n' \
                          '  </tr>' \
                          '</table>\n'
                          % (block_title, block_indexlink, block_dllink, block_editlink, block_abstract))

        if layout=='compact':
            box.write('</table>\n')

        # The DocTable can carry along its own search form that stays in sync
        # for filtering the data. Insert it here if show_search was passed in.
        if show_search==1 and lampadasweb.static==0:
            box.write(self.tabsearch(uri, title=title,
                                          short_title=short_title,
                                          pub_status_code=pub_status_code,
                                          type_code=type_code,
                                          topic_code=topic_code,
                                          username=username,
                                          maintained=maintained,
                                          maintainer_wanted=maintainer_wanted,
                                          lang=lang,
                                          review_status_code=review_status_code,
                                          tech_review_status_code=tech_review_status_code,
                                          pub_date=pub_date,
                                          last_update=last_update,
                                          tickle_date=tickle_date,
                                          isbn=isbn,
                                          rating=rating,
                                          format_code=format_code,
                                          dtd_code=dtd_code,
                                          license_code=license_code,
                                          copyright_holder=copyright_holder,
                                          sk_seriesid=sk_seriesid,
                                          abstract=abstract,
                                          short_desc=short_desc,
                                          collection_code=collection_code,
                                          layout=layout))

        return box.get_value()

    def tabdocument_icon_box(self, uri):
        """Returns a navigation box of document icons."""

        box = WOStringIO('<table><tr>%s</tr></table>'
                        % (self.document_icon_cells(uri.id)))
        return box.get_value()
        
    def document_icon_cells(self, doc_id, cell_type='td'):
        """Returns a series of cells populated with icons for the document."""

        doc = lampadas.docs[doc_id]

        # Link to the online output
        if doc.pub_time > '':
            box = WOStringIO('<%s width=22><a href="|uri.base|doc/%s/index.html">%s</a></%s>\n'
                            % (cell_type,str(doc.id), HTML_ICON_SM, cell_type))
        else:
            box = WOStringIO('<%s></%s>\n' % (cell_type, cell_type))
        
        # Folder icon
        if doc.mirror_time > '':
            box.write('<%s width=22><a href="|uri.base|docdownloads/%s/">%s</a></%s>\n'
                     % (cell_type, str(doc.id), FOLDER_ICON_SM, cell_type))
        else:
            box.write('<%s></%s>\n' % (cell_type, cell_type))
            
        # View icon
        box.write('<%s width=22><a href="|uri.base|view_document/%s|uri.lang_ext|">%s</a></%s>\n'
                  % (cell_type, str(doc.id), VIEW_ICON_SM, cell_type))

        # Edit icon
        if sessions.session and sessions.session.user.can_edit(doc_id=doc.id)==1:
            box.write('<%s width=22><a href="|uri.base|document_main/%s|uri.lang_ext|">%s</a></%s>\n'
                      % (cell_type, str(doc.id), EDIT_ICON_SM, cell_type))
        else:
            box.write('<%s width=22></%s>\n'
                      % (cell_type, cell_type))

        return box.get_value()
       
    def userdocs(self, uri, username=''):
        """
        Displays a DocTable containing documents linked to a user.
        The default is to display docs for the logged-on user,
        but you can override that.
        """
        if sessions.session==None:
            return '|nopermission|'
        if sessions.session.user.can_edit(username=username)==0:
            return '|nopermission|'
        if username > '':
            return self.doctable(uri, username=username, show_search=0)
        else:
            return self.doctable(uri, username=sessions.session.username, show_search=0)

    def section_menu(self, uri, section_code):
        log(3, "Creating section menu: " + section_code)
        section = lampadasweb.sections[section_code]
        box = WOStringIO('<table class="navbox"><tr><th>%s</th></tr>\n' \
                         '<tr><td>' % section.name[uri.lang])
        keys = lampadasweb.pages.sort_by('sort_order')
        for key in keys:
            page = lampadasweb.pages[key]
            if page.section_code==section.code:
                if lampadasweb.static and page.only_dynamic:
                    continue
                if page.only_registered and sessions.session==None:
                    continue
                if page.only_admin and (sessions.session==None or sessions.session.user.admin==0):
                    continue
                if page.only_sysadmin and (sessions.session==None or sessions.session.user.sysadmin==0):
                    continue
                menu_name = page.menu_name[uri.lang]
                menu_name = menu_name.replace(' ', '&nbsp;')
                box.write('<a href="|uri.base|%s|uri.lang_ext|">%s</a><br>\n' 
                    % (page.code, menu_name))
        box.write('</td></tr></table>\n')
        return box.get_value()

    def section_menus(self, uri):
        log(3, "Creating all section menus")
        box = WOStringIO('')
        keys = lampadasweb.sections.sort_by('sort_order')
        menu_separator = ''
        for key in keys:
            section = lampadasweb.sections[key]
            if lampadasweb.static and section.static_count==0:
                continue
            if section.nonregistered_count==0 and (sessions.session==None):
                continue
            if section.nonadmin_count==0 and (sessions.session==None or sessions.session.user.admin==0):
                continue
            if section.nonsysadmin_count==0 and (sessions.session==None or sessions.session.user.sysadmin==0):
                continue
            box.write(menu_separator + self.section_menu(uri, section.code))
            menu_separator = '<p>'
        return box.get_value()

    def sitemap(self, uri):
        log(3, 'Creating sitemap')
        box = WOStringIO('')
        section_codes = lampadasweb.sections.sort_by('sort_order')
        page_codes = lampadasweb.pages.sort_by('sort_order')
        for section_code in section_codes:
            section = lampadasweb.sections[section_code]
            if section.static_count==0 and lampadasweb.static:
                continue
            if section.nonregistered_count==0 and sessions.session==None:
                continue
            if section.nonadmin_count==0 and (sessions.session==None or sessions.session.user.admin==0):
                continue
            if section.nonsysadmin_count==0 and (sessions.session==None or sessions.session.user.sysadmin==0):
                continue

            odd_even = OddEven()
            box.write('<p><table class="box" width="100%%"><tr><th>%s</th></tr>\n'
                      % section.name[uri.lang])
            for page_code in page_codes:
                page = lampadasweb.pages[page_code]
                if page.section_code==section_code:
                    if page.only_dynamic and lampadasweb.static:
                        continue
                    if page.only_registered or page.only_admin or page.only_sysadmin > 0:
                        if sessions.session==None: continue
                    if page.only_admin > 0:
                        if sessions.session==None: continue
                        if sessions.session.user.admin==0 and sessions.session.user.sysadmin==0:
                            continue
                    if page.only_sysadmin > 0:
                        if sessions.session==None: continue
                        if sessions.session.user.sysadmin==0:
                            continue
                    box.write('<tr class="%s"><td><a href="|uri.base|%s|uri.lang_ext|">%s</a></td></tr>\n'
                              % (odd_even.get_next(), page.code, page.menu_name[uri.lang]))
            box.write('</table>\n')
        return box.get_value()

    def navtopics(self, uri):
        if self['navtopics']==None:
            self['navtopics'] = LampadasCollection()
            self['navtopics'].html = LampadasCollection()
        if self['navtopics'].html[uri.lang]==None:
            log(3, 'Creating navtopics menu')
            box = WOStringIO('''<table class="navbox">
            <tr><th>|strtopics|</th></tr>
            <tr><td>''')
            keys = lampadas.topics.sort_by('sort_order')
            for key in keys:
                topic = lampadas.topics[key]
                if topic.parent_code=='':
                    box.write('<a href="|uri.base|topic/%s|uri.lang_ext|">%s</a><br>\n'
                              % (topic.code, topic.name[uri.lang]))
            box.write('</td></tr></table>\n')
            self['navtopics'].html[uri.lang] = box.get_value()
        return self['navtopics'].html[uri.lang]

    def tabtopics(self, uri):
        log(3, 'Creating tabtopics table')
        topic = lampadas.topics[uri.code]
        box = WOStringIO('''<table class="box" width="100%%">
        <tr><th>%s</th></tr>
        <tr><th class="collabel">|topic.description|</th></tr>
        ''' % topic.title[uri.lang])
        keys = lampadas.topics.sort_by('sort_order') 
        odd_even = OddEven()
        for key in keys:
            topic = lampadas.topics[key]
            if topic.parent_code==uri.code:
                box.write('<tr class="%s"><td><a href="|uri.base|topic/%s|uri.lang_ext|">%s</a></td></tr>\n'
                          % (odd_even.get_next(), topic.code, topic.name[uri.lang]))
        box.write('</td></tr>\n</table>\n')
        return box.get_value()

    def tabtopic(self, uri):
        log(3, 'Creating tabtopic table')
        topic = lampadas.topics[uri.code]
        box = '''<table class="box nontabular" width="100%%">
        <tr><th>%s</th></tr>
        <tr><td>%s</td><tr>
        </table>
        ''' % (topic.title[uri.lang], topic.description[uri.lang])
        return box

    def navtypes(self, uri):
        log(3, 'Creating types menu')
        box = WOStringIO('''<table class="navbox">
        <tr><th>|strtypes|</th></tr>
        <tr><td>''')
        keys = lampadas.types.sort_by('sort_order')
        for key in keys:
            type = lampadas.types[key]
            box.write('<a href="|uri.base|type/%s|uri.lang_ext|">%s</a><br>\n'
                      % (type.code, type.name[uri.lang]))
        box.write('</td></tr>\n</table>\n')
        return box.get_value()

    def navcollections(self, uri):
        log(3, 'Creating collections menu')
        box = WOStringIO('''<table class="navbox">
        <tr><th>|strcollections|</th></tr>
        <tr><td>''')
        keys = lampadas.collections.sort_by('sort_order')
        for key in keys:
            collection = lampadas.collections[key]
            box.write('<a href="|uri.base|collection/%s|uri.lang_ext|">%s</a><br>\n'
                      % (collection.code, collection.name[uri.lang]))
        box.write('</td></tr>\n</table>\n')
        return box.get_value()

    def tabcollections(self, uri):
        log(3, 'Creating collections table')
        box = WOStringIO('''<table class="box">
        <tr><th colspan="2">|strcollections|</th></tr>''')
        keys = lampadas.collections.sort_by('sort_order')
        for key in keys:
            collection = lampadas.collections[key]
            box.write('<tr><td><a href="|uri.base|collection/%s|uri.lang_ext|">%s</a></td>\n' \
                      '    <td>%s</td>\n' \
                      '</tr>'
                      % (collection.code, collection.name[uri.lang], collection.description[uri.lang]))
        box.write('</td></tr>\n</table>\n')
        return box.get_value()

    def tabcollection(self, uri):
        log(3, 'Creating collection table')
        return self.doctable(uri, collection_code=uri.code)

    def navlogin(self, uri):
        if lampadasweb.static==1:
            return ''
        if sessions.session:
            log(3, 'Creating active user box')
            box = '''<table class="navbox">
            <tr><th>|stractive_user|</th></tr>
            <form name="logout" action="|uri.base|data/session/logout">
            <input name="username" type="hidden" value="%s">
            <tr><td align="center">
            <a href="|uri.base|user/|session_username||uri.lang_ext|">|session_name|</a>
            <p>
            <input type="submit" name="logout"
            value="|strlog_out|"></td></tr>
            </form>
            </table>
            ''' % sessions.session.username
        else:
            log(3, 'Creating login box')
            box = '''<table class="navbox">
            <tr><th colspan="2">|strlogin|</th></tr>
            <form name="login" action="|uri.base|data/session/login" method="GET">
            <tr>
              <td class="label">|strusername|</td>
              <td><input type="text" name="username" size="10"></td>
            </tr>
            <tr>
              <td class="label">|strpassword|</td>
              <td><input type="password" name="password" size="10"></td>
            </tr>
            <tr>
              <td align="center" colspan="2">
              <input type=submit name="login" value="login"><br>
              <a href="|uri.base|mailpass|uri.lang_ext|">|strmail_passwd|</a><br>
              <a href="|uri.base|newuser|uri.lang_ext|">|strcreate_acct|</a></td>
            </tr>
            </form> 
            </table>
            '''
        return box

    def navsessions(self, uri):
        if sessions.session and sessions.session.user.admin > 0:
            log(3, 'Creating navsessions table')
            box = WOStringIO('''<table class="navbox">
            <tr><th>|strsessions|</th></tr>
            <tr><td>
            ''')
            keys = sessions.sort_by('username')
            for key in keys:
                session = sessions[key]
                box.write('<a href="|uri.base|user/%s|uri.lang_ext|">%s</a><br>\n'
                          % (session.username, session.username))
            box.write('</td></tr>\n</table>\n')
            return box.get_value()
        return ''

    def tabsessions(self, uri):
        if sessions.session.user and sessions.session.user.admin > 0:
            log(3, 'Creating sessions table')
            box = WOStringIO('''<table class="box" width="100%">
            <tr><th colspan="4">|strsessions|</th></tr>
            <tr>
            <th class="collabel">|strusername|</th>
            <th class="collabel">|strip_address|</th>
            <th class="collabel">|strurl|</th>
            <th class="collabel">|strtimestamp|</th>
            </tr>
            ''')
            keys = sessions.sort_by_desc('created')
            odd_even = OddEven()
            for key in keys:
                session = sessions[key]
                box.write('''<tr class="%s">
                <td><a href="|uri.base|user/%s|uri.lang_ext|">%s</a></td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                </tr>
                ''' % (odd_even.get_next(),
                       session.username, session.username,
                       session.ip_address,
                       session.uri,
                       session.created))
            box.write('</table>\n')
            return box.get_value()
        return '|nopermission|'

    def navlanguages(self, uri):
        log(3, 'Creating languages table')
        box = WOStringIO('''<table class="navbox">
        <tr><th>|strlanguages|</th></tr>
        <tr><td>
        ''')
        keys = languages.sort_by_lang('name', uri.lang)
        for key in keys:
            language = languages[key]
            if language.supported > 0:
                if uri.data > '':
                    add_data = '/' + uri.data
                else:
                    add_data = ''
                add_data = string.join(uri.data,'/')
                if add_data > '':
                    add_data = '/' + add_data
                box.write('<a href="|uri.base|%s%s.%s.html">%s</a><br>\n'
                          % (uri.page_code,
                             add_data,
                             language.code.lower(),
                             language.name[uri.lang]))
        box.write('</td></tr>\n</table>\n')
        return box.get_value()

    def tabsearch(self, uri, title='', short_title='', pub_status_code='', type_code='', topic_code='',
                    username='', maintained='', maintainer_wanted='', lang='', review_status_code='',
                    tech_review_status_code='', pub_date='', last_update='', tickle_date='',
                    isbn='', rating='', format_code='', dtd_code='', license_code='',
                    copyright_holder='', sk_seriesid='', abstract='', short_desc='', collection_code='',
                    layout='compact'):
        log(3, 'Creating tabsearch table')
        box = WOStringIO()
        box.write('''
            <table class="box">\n
            <form name="search" action="|uri.base|data/search/document">
            <tr><th colspan="2">|strsearch|</th></tr>\n
            <tr><td class="label">|strtitle|</td><td>%s</td></tr>
            <tr><td class="label">|strshort_title|</td><td>%s</td></tr>
            <tr><td class="label">|strstatus|</td><td>%s</td></tr>
            <tr><td class="label">|strtype|</td><td>%s</td></tr>
            <tr><td class="label">|strtopic|</td><td>%s</td></tr>
            <tr><td class="label">|strusername|</td><td>%s</td></tr>
            <tr><td class="label">|strmaintained|</td><td>%s</td></tr>
            <tr><td class="label">|strmaint_wanted|</td><td>%s</td></tr>
            <tr><td class="label">|strlanguage|</td><td>%s</td></tr>
            <tr><td class="label">|strwriting|</td><td>%s</td></tr>
            <tr><td class="label">|straccuracy|</td><td>%s</td></tr>
            <tr><td class="label">|strpub_date|</td><td>%s</td></tr>
            <tr><td class="label">|strupdated|</td><td>%s</td></tr>
            <tr><td class="label">|strtickle_date|</td><td>%s</td></tr>
            <tr><td class="label">|strisbn|</td><td>%s</td></tr>
            <tr><td class="label">|strrating|</td><td>%s</td></tr>
            <tr><td class="label">|strformat|</td><td>%s</td></tr>
            <tr><td class="label">|strdtd|</td><td>%s</td></tr>
            <tr><td class="label">|strlicense|</td><td>%s</td></tr>
            <tr><td class="label">|strcopyright_holder|</td><td>%s</td></tr>
            <tr><td class="label">|strtrans_master|</td><td>%s</td></tr>
            <tr><td class="label">|strabstract|</td><td>%s</td></tr>
            <tr><td class="label">|strshort_desc|</td><td>%s</td></tr>
            <tr><td class="label">|strcollection|</td><td>%s</td></tr>
            <tr><td class="label">|strlayout|</td><td>%s</td></tr>
            <tr><td></td><td><input type="submit" value="|strsearch|"></td></tr>
            </form>
            </table>
            '''
            % (widgets.title(title),
               widgets.short_title(short_title),
               widgets.pub_status_code(pub_status_code, uri.lang),
               widgets.type_code(type_code, uri.lang),
               widgets.topic_code(topic_code, uri.lang),
               widgets.username(username),
               widgets.tf('maintained', maintained),
               widgets.tf('maintainer_wanted', maintainer_wanted),
               widgets.doc_lang(lang, uri.lang),
               widgets.review_status_code(review_status_code, uri.lang),
               widgets.tech_review_status_code(tech_review_status_code, uri.lang),
               widgets.pub_date(pub_date),
               widgets.last_update(last_update),
               widgets.tickle_date(tickle_date),
               widgets.isbn(isbn),
               widgets.rating(rating),
               widgets.format_code(format_code, uri.lang),
               widgets.dtd_code(dtd_code, uri.lang),
               widgets.license_code(license_code, uri.lang),
               widgets.copyright_holder(copyright_holder),
               widgets.sk_seriesid(sk_seriesid),
               widgets.abstract(abstract),
               widgets.short_desc(short_desc),
               widgets.collection_code(collection_code, uri.lang),
               widgets.doctable_layout(layout)
               ))
        return box.get_value()

    def tablint_time_stats(self, uri):
        log(3, 'Creating lint_time_stats table')
        box = WOStringIO('<table class="box">\n' \
                         '<tr><th colspan="3">|strlint_time_stats|</th></tr>\n' \
                         '<tr><th class="collabel">|strlint_time|</th>\n' \
                             '<th class="collabel" align="right">|strcount|</th>\n' \
                             '<th class="collabel" align="right">|strpct|</th>\n' \
                         '</tr>\n')
        stattable = stats['lint_time']
        odd_even = OddEven()
        for key in stattable.sort_by('label'):
            stat = stattable[key]
            box.write('<tr class="%s"><td class="label">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                      '</tr>\n'
                      % (odd_even.get_next(), stat.label, stat.value, fpformat.fix(stattable.pct(key) * 100, 2)))
        box.write('<tr class="%s"><td class="label">|strtotal|</td>\n' \
                      '<td align="right">%s</td><td></td>\n' \
                  '</tr></table>'
                  % (odd_even.get_next(), stattable.sum()))
        return box.get_value()
        
    def tabmirror_time_stats(self, uri):
        log(3, 'Creating mirror_time_stats table')
        box = WOStringIO('<table class="box">\n' \
                         '<tr><th colspan="3">|strmirror_time_stats|</th></tr>\n' \
                         '<tr><th class="collabel">|strmirror_time|</th>\n' \
                             '<th class="collabel" align="right">|strcount|</th>\n' \
                             '<th class="collabel" align="right">|strpct|</th>\n' \
                         '</tr>\n')
        stattable = stats['mirror_time']
        odd_even = OddEven()
        for key in stattable.sort_by('label'):
            stat = stattable[key]
            box.write('<tr class="%s"><td class="label">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                      '</tr>\n'
                      % (odd_even.get_next(), stat.label, stat.value, fpformat.fix(stattable.pct(key) * 100, 2)))
        box.write('<tr class="%s"><td class="label">|strtotal|</td>\n' \
                      '<td align="right">%s</td><td></td>\n' \
                  '</tr></table>'
                  % (odd_even.get_next(), stattable.sum()))
        return box.get_value()
        
    def tabpub_time_stats(self, uri):
        log(3, 'Creating pub_time_stats table')
        box = WOStringIO('<table class="box">\n' \
                         '<tr><th colspan="3">|strpub_time_stats|</th></tr>\n' \
                         '<tr><th class="collabel">|strpub_time|</th>\n' \
                             '<th class="collabel" align="right">|strcount|</th>\n' \
                             '<th class="collabel" align="right">|strpct|</th>\n' \
                         '</tr>\n')
        stattable = stats['pub_time']
        odd_even = OddEven()
        for key in stattable.sort_by('label'):
            stat = stattable[key]
            box.write('<tr class="%s"><td class="label">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                      '</tr>\n'
                      % (odd_even.get_next(), stat.label, stat.value, fpformat.fix(stattable.pct(key) * 100, 2)))
        box.write('<tr class="%s"><td class="label">|strtotal|</td>\n' \
                      '<td align="right">%s</td><td></td>\n' \
                  '</tr></table>'
                  % (odd_even.get_next(), stattable.sum()))
        return box.get_value()
        
    def tabpub_status_stats(self, uri):
        log(3, 'Creating pub_status_stats table')
        box = WOStringIO('<table class="box">\n' \
                         '<tr><th colspan="3">|strpub_status_stats|</th></tr>\n' \
                         '<tr><th class="collabel">|strstatus|</th>\n' \
                             '<th class="collabel" align="right">|strcount|</th>\n' \
                             '<th class="collabel" align="right">|strpct|</th>\n' \
                         '</tr>\n')
        stattable = stats['pub_status']
        odd_even = OddEven()
        for key in lampadas.pub_statuses.sort_by('sort_order'):
            stat = stattable[key]
            if stat==None:
                stat = Stat()
            box.write('<tr class="%s"><td class="label">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                      '</tr>\n'
                      % (odd_even.get_next(),
                        lampadas.pub_statuses[key].name[uri.lang], 
                        stat.value, 
                        fpformat.fix(stattable.pct(key) * 100, 2)))
        box.write('<tr class="%s"><td class="label">|strtotal|</td>\n' \
                      '<td align="right">%s</td><td></td>\n' \
                  '</tr></table>'
                  % (odd_even.get_next(), stattable.sum()))
        return box.get_value()
        
    def tabdoc_error_stats(self, uri):
        log(3, 'Creating doc_error_stats table')
        box = WOStringIO('<table class="box">\n' \
                         '<tr><th colspan="4">|strdoc_error_stats|</th></tr>\n' \
                         '<tr><th class="collabel">|strid|</th>\n' \
                             '<th class="collabel">|strerror|</th>\n' \
                             '<th class="collabel">|strtype|</th>\n' \
                             '<th class="collabel" align="right">|strcount|</th>\n' \
                         '</tr>\n')
        stattable = stats['doc_error']
        odd_even = OddEven()
        for key in stattable.sort_by('label'):
            stat = stattable[key]
            error = errors[key]
            errortype = errortypes[error.err_type_code]
            box.write('<tr class="%s"><td class="label">%s</td>\n' \
                          '<td>%s</td>\n' \
                          '<td>%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                      '</tr>\n'
                      % (odd_even.get_next(),
                        stat.label, 
                        errortype.name[uri.lang],
                        error.name[uri.lang], 
                        stat.value))
        box.write('<tr class="%s"><td class="label">|strtotal|</td>\n' \
                      '<td></td><td></td><td align="right">%s</td>\n' \
                  '</tr></table>'
                  % (odd_even.get_next(), stattable.sum()))
        return box.get_value()
        
    def tabdoc_format_stats(self, uri):
        log(3, 'Creating doc_format_stats table')
        box = WOStringIO('<table class="box">\n' \
                         '<tr><th colspan="3">|strdoc_format_stats|</th></tr>\n' \
                         '<tr><th class="collabel">|strformat|</th>\n' \
                             '<th class="collabel" align="right">|strcount|</th>\n' \
                             '<th class="collabel" align="right">|strpct|</th>\n' \
                         '</tr>\n')
        stattable = stats['doc_format']
        odd_even = OddEven()
        for key in lampadas.formats.sort_by_lang('name', uri.lang):
            stat = stattable[key]
            if stat==None:
                stat = Stat()
            box.write('<tr class="%s"><td class="label">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                      '</tr>\n'
                      % (odd_even.get_next(),
                        lampadas.formats[key].name[uri.lang], 
                        stat.value, 
                        fpformat.fix(stattable.pct(key) * 100, 2)))
        box.write('<tr class="%s"><td class="label">|strtotal|</td>\n' \
                      '<td align="right">%s</td><td></td>\n' \
                  '</tr></table>'
                  % (odd_even.get_next(), stattable.sum()))
        return box.get_value()
        
    def tabdoc_dtd_stats(self, uri):
        log(3, 'Creating doc_dtd_stats table')
        box = WOStringIO('<table class="box">\n' \
                         '<tr><th colspan="3">|strdoc_dtd_stats|</th></tr>\n' \
                         '<tr><th class="collabel">|strdtd|</th>\n' \
                             '<th class="collabel" align="right">|strcount|</th>\n' \
                             '<th class="collabel" align="right">|strpct|</th>\n' \
                         '</tr>\n')
        stattable = stats['doc_dtd']
        odd_even = OddEven()
        for key in lampadas.dtds.sort_by('code'):
            stat = stattable[key]
            if stat==None:
                stat = Stat()
            box.write('<tr class="%s"><td class="label">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                      '</tr>\n'
                      % (odd_even.get_next(),
                        lampadas.dtds[key].code, 
                        stat.value, 
                        fpformat.fix(stattable.pct(key) * 100, 2)))
        box.write('<tr class="%s"><td class="label">|strtotal|</td>\n' \
                      '<td align="right">%s</td><td></td>\n' \
                  '</tr></table>'
                  % (odd_even.get_next(), stattable.sum()))
        return box.get_value()
        
    def tabdoc_lang_stats(self, uri):
        log(3, 'Creating doc_lang_stats table')
        box = WOStringIO('<table class="box">\n' \
                         '<tr><th colspan="4">|strdoc_lang_stats|</th></tr>\n' \
                         '<tr><th class="collabel">|strlanguage_code|</th>\n' \
                             '<th class="collabel">|strlanguage|</th>\n' \
                             '<th class="collabel" align="right">|strcount|</th>\n' \
                             '<th class="collabel" align="right">|strpct|</th>\n' \
                         '</tr>\n')
        stattable = stats['doc_lang']
        odd_even = OddEven()
        for key in languages.sort_by_lang('name', uri.lang):
            stat = stattable[key]
            if stat==None:
                stat = Stat()
            box.write('<tr class="%s"><td class="label">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                      '</tr>\n'
                      % (odd_even.get_next(),
                        languages[key].code, 
                        languages[key].name[uri.lang],
                        stat.value, 
                        fpformat.fix(stattable.pct(key) * 100, 2)))
        box.write('<tr class="%s"><td class="label">|strtotal|</td>\n' \
                      '<td align="right">%s</td><td></td>\n' \
                  '</tr></table>'
                  % (odd_even.get_next(), stattable.sum()))
        return box.get_value()
        
    def tabmailpass(self, uri):
        log(3, 'Creating mailpass table')
        box = '''<form name="mailpass" action="|uri.base|data/save/mailpass">
        <table class="box" width="100%">
        <tr><th colspan="2">|strmail_passwd|</th></tr>
        <tr>
        <td><input type="text" name="email"></td>
        <td align="center"><input type="submit" name="mailpass" value="|strmail_passwd|"></td></tr>
        </table>
        </form>
        '''
        return box

    def tabsplashlanguages(self, uri):
        """Creates a customizable splash page for selecting a language.
           Each element gets a unique identifier such as 'p1', so a css
           stylesheet can exercise fine control over placement."""
        log(3, 'Creating tabslashlanguages table')
        box = WOStringIO('<p class="hide"><div class="map">\n' \
                         '<h1 id="p1">|strproject|</h1>\n')
        id = 1
        for key in languages.supported_keys(uri.lang):
            id = id + 1
            language = languages[key]
            box.write('<p id="p%s"><a href="%s.%s.html">%s</a></p>\n'
                % (str(id), 'home', key.lower(), language.name[language.code]))
        box.write('</div>')
        return box.get_value()

    def tabdocument_tabs(self, uri):
        document = lampadas.docs[uri.id]
        box = WOStringIO('<table class="tab"><tr>\n')
       
        # Determine which tab is selected and establish classes.
        main_selected         = ''
        files_selected        = ''
        versions_selected     = ''
        topics_selected       = ''
        users_selected        = ''
        notes_selected        = ''
        translations_selected = ''
        errors_selected1      = ''
        errors_selected2      = ''
        admin_selected        = ''
        all_selected          = ''
        if uri.page_code=='document_main':
            main_selected           = ' class="selected_tab"'
        elif uri.page_code=='document_files':
            files_selected          = ' class="selected_tab"'
        elif uri.page_code=='document_revs':
            versions_selected       = ' class="selected_tab"'
        elif uri.page_code=='document_topics':
            topics_selected         = ' class="selected_tab"'
        elif uri.page_code=='document_users':
            users_selected          = ' class="selected_tab"'
        elif uri.page_code=='document_notes':
            notes_selected          = ' class="selected_tab"'
        elif uri.page_code=='document_translation':
            translations_selected   = ' class="selected_tab"'
        elif uri.page_code=='document_errors':
            errors_selected1   = '  selected_tab'
            errors_selected2   = ' class="selected_tab"'
        elif uri.page_code=='document_admin':
            admin_selected   = ' class="selected_tab"'
        elif uri.page_code=='document':
            all_selected            = ' class="selected_tab"'

        # Write the tags, inserting the class on the erorrs tab.
        box.write('<th%s"><a href="|uri.base|document_main/|uri.id||uri.lang_ext|">|strdetails|</a></th>\n' % (main_selected))
        box.write('<th%s><a href="|uri.base|document_files/|uri.id||uri.lang_ext|">|strfiles|</a></th>\n' % (files_selected))
        box.write('<th%s><a href="|uri.base|document_revs/|uri.id||uri.lang_ext|">|strversions|</a></th>\n' % (versions_selected))
        box.write('<th%s><a href="|uri.base|document_topics/|uri.id||uri.lang_ext|">|strtopics|</a></th>\n' % (topics_selected))
        box.write('<th%s><a href="|uri.base|document_users/|uri.id||uri.lang_ext|">|strusers|</a></th>\n' % (users_selected))
        box.write('<th%s><a href="|uri.base|document_notes/|uri.id||uri.lang_ext|">|strnotes|</a></th>\n' % (notes_selected))
        box.write('<th%s><a href="|uri.base|document_translation/|uri.id||uri.lang_ext|">|strtranslations|</a></th>\n' % (translations_selected))
        if document.errors.count() > 0 or document.files.error_count > 0:
            box.write('<th class="error%s"><a href="|uri.base|document_errors/|uri.id||uri.lang_ext|">|strerrors|</a></th>\n' % (errors_selected1))
        else:
            box.write('<th%s><a href="|uri.base|document_errors/|uri.id||uri.lang_ext|">|strerrors|</a></th>\n' % (errors_selected2))
        box.write('<th%s><a href="|uri.base|document_admin/|uri.id||uri.lang_ext|">|stradmin|</a></th>\n' % (admin_selected))
        box.write('<th%s><a href="|uri.base|document/|uri.id||uri.lang_ext|">|strall|</a></th>\n' % (all_selected))
        box.write('</tr></table>\n')
        return box.get_value()

# Eventually these will be user-editable, and expandable by writing your own
# classes to be loaded into this collection. I'm gradually moving the above routines
# into classes here. Later, I'll put each of these in their own file, all in a separate
# directory, then load them dynamically into the interpreter.

# We might use a templating engine (Cheetah?) to generate these from more easily
# editable templates at some point. Could just use m4 though.

# When moving a routine into a class, you have to remove it from the HTML.py module.

class Table:

    def __init__(self, code, method):
        self.code   = code
        self.method = method

    def __call__(self, uri):
        return self.method(uri)
   
class DocTable(Table):

    def __init__(self):
        Table.__init__(self, 'doctable', self.method)

    def method(self, uri):
        return tables.doctable(uri, lang=uri.lang, layout='compact')

class DocTableExpanded(Table):

    def __init__(self):
        Table.__init__(self, 'doctableexpanded', self.method)

    def method(self, uri):
        return tables.doctable(uri, lang=uri.lang, layout='expanded')

class DocAdmin(Table):
    
    def __init__(self):
        Table.__init__(self, 'docadmin', self.method)

    def method(self, uri):
        """Returns a set of controls for publishing documents."""

        # FIXME: Only 'N'ormal documents should be publishable!

        if sessions.session and sessions.session.user.can_edit(uri.id)==1:
            doc = lampadas.docs[uri.id]
            box = WOStringIO('<table class="box nontabular"><tr><th colspan="4">|strdoc_admin|</th></tr>\n' \
                             '<tr><td class="label">|strdoc_check_errors|</td>\n' \
                             '    <td><a href="|uri.base|data/admin/run_lintadas?doc_id=%s">|strrun|</a></td>\n' \
                             '    <td class="label">|strlint_time|</td>\n' \
                             '    <td>%s</td></tr>\n' \
                             '<tr><td class="label">|strdoc_mirror|</td>\n' \
                             '    <td><a href="|uri.base|data/admin/run_mirror?doc_id=%s">|strrun|</a></td>\n' \
                             '    <td class="label">|strmirror_time|</td>\n' \
                             '    <td>%s</td></tr>\n' \
                             '<tr><td class="label">|strdoc_publish|</td>\n' \
                             '    <td><a href="|uri.base|data/admin/run_publish?doc_id=%s">|strrun|</a></td>\n' \
                             '    <td class="label">|strpub_time|</td>\n' \
                             '    <td>%s</td></tr>\n' \
                             '</table>'
                             % (doc.id, doc.lint_time, doc.id, doc.mirror_time, doc.id, doc.pub_time))

            return box.get_value()
        else:
            return '|blknopermission|'


# The off-by-one error is intentional. If 0 is passed in items, we never
# stop processing items, but list them all intead.

class TabNews(Table):

    def __init__(self, items=0):
        Table.__init__(self, 'news', self.method)
        self.items = items

    def method(self, uri):
        log(3, 'Creating recent news')
        box = WOStringIO('<table class="box nontabular" width="100%">'
                         '<tr><th colspan="2">|strnews|</th></tr>')
        keys = lampadasweb.news.sort_by_desc('pub_date')
        items = 0
        for key in keys:
            news = lampadasweb.news[key]
            if not news.news[uri.lang]==None:
                if sessions.session and sessions.session.user.can_edit(news_id=news.id)==1:
                    edit_icon = '<a href="|uri.base|news_edit/' + str(news.id) + '|uri.lang_ext|">' + EDIT_ICON_SM + '</a>\n'
                else:
                    edit_icon = ''

                box.write('<tr><th class="sectionlabel" colspan="2">%s %s</th></tr>\n'
                          '<tr class="odd"><td class="label">%s</td>\n'
                          '               <td>%s</td>\n'
                          '</tr>\n'
                          % (edit_icon,
                             news.headline[uri.lang],
                             news.pub_date,
                             news.news[uri.lang]))
            items = items + 1
            if items==self.items:
                break
        box.write('</table>\n')
        return box.get_value()

class TabNewsItem(Table):

    def __init__(self):
        Table.__init__(self, 'news', self.method)

    def method(self, uri):
        if not sessions.session:
            return '|blknopermission|'
        elif sessions.session.user.can_edit(news_id=uri.id)==0:
            return '|blknopermission|'

        if uri.id > 0:
            news = lampadasweb.news[uri.id]

            box = WOStringIO('<form method=GET action="|uri.base|data/save/news">\n' \
                             '<table class="box nontabular"><tr><th colspan="3">|strnews|</th></tr>\n' \
                             '<input type=hidden name="news_id" value="%s">\n' \
                             '<tr><td class="label">|strpub_date|</td>\n' \
                             '    <td><input type=text name="pub_date" value="%s"></td>\n' \
                             '    <td><input type=submit name="save" value="|strsave|"></td>\n' \
                             '</tr>\n' \
                             '</table>\n' \
                             '</form>\n' % (news.id, news.pub_date))

            # List the available translations
            box.write('<table class="box" style="width:100%"><tr><th colspan="3">|strtranslations|</th></tr>\n')

            odd_even = OddEven()
            for lang in languages.supported_keys(uri.lang):
                if not news.news[lang]==None:
                    box.write('<form method=GET action="|uri.base|data/save/news_lang">\n' \
                              '<input type=hidden name="news_id" value="%s">\n' \
                              '<input type=hidden name="lang" value="%s">\n' \
                              '<tr class="%s"><td class="sectionlabel" colspan="3">%s</td></tr>\n' \
                              '<tr class="%s"><td class="label">|strversion|</td><td>%s</td>\n<td></td></tr>\n' \
                              '<tr class="%s"><td class="label">|strheadline|</td><td>%s</td><td></td></tr>\n' \
                              '<tr class="%s"><td class="label">|strnews|</td><td>%s</td><td>%s</td></tr>' \
                              '</form>'
                              % (news.id, lang,
                                 odd_even.get_next(), languages[lang].name[uri.lang],
                                 odd_even.get_last(), widgets.version(news.version[lang]),
                                 odd_even.get_last(), widgets.headline(news.headline[lang]),
                                 odd_even.get_last(), widgets.news(news.news[lang]),
                                 widgets.save()))

            # Add a new translation if there are untranslated languages.
            if len(news.untranslated_lang_keys(uri.lang)) > 0:
                box.write('<form method=GET action="|uri.base|data/save/newnews_lang">\n' \
                          '<input type=hidden name="news_id" value="%s">\n' \
                          '<tr class="%s"><td class="sectionlabel" colspan="3">|stradd_translation|</td></tr>' \
                          '<tr class="%s"><td class="label">|strlanguage|</td><td>%s</td>\n<td></td></tr>\n' \
                          '<tr class="%s"><td class="label">|strversion|</td><td>%s</td>\n<td></td></tr>\n' \
                          '<tr class="%s"><td class="label">|strheadline|</td><td>%s</td></tr>\n' \
                          '<tr class="%s"><td class="label">|strnews|</td><td>%s</td><td>%s</td></tr>' \
                          '</form>'
                          % (news.id, odd_even.get_next(),
                             odd_even.get_last(), widgets.new_news_lang(news.id, uri.lang),
                             odd_even.get_last(), widgets.version('1.0'),
                             odd_even.get_last(), widgets.headline(''),
                             odd_even.get_last(), widgets.news(''),
                             widgets.save()))
            box.write('</table>')
        else:
            news = NewsItem()
            box = WOStringIO('<form method=GET action="|uri.base|data/save/newnews">\n' \
                             '<table class="box"><tr><th colspan="3">|stradd_news|</th></tr>\n' \
                             '<tr class="odd"><td class="label">|strpub_date|</td>\n' \
                             '    <td><input type=text name="pub_date" value="%s"></td>\n' \
                             '    <td colspan="2"><input type=submit name="save" value="|stradd|"></td>\n' \
                             '</tr>\n' \
                             '</table>\n' \
                             '</form>\n' % (news.pub_date))
            
        return box.get_value()
        
class TabPages(Table):

    def __init__(self):
        Table.__init__(self, 'pages', self.method)

    def method(self, uri):
        log(3, 'Creating pages table')
        box = WOStringIO('<table class="box" width="100%%">\n' \
                         '<tr><th colspan="5">|strpages|</th></tr>\n' \
                         '<tr><th class="collabel" colspan="2">|strpage_code|</th>\n' \
                         '    <th class="collabel">|strtemplate|</th>\n' \
                         '    <th class="collabel">|strsection|</th>\n' \
                         '    <th class="collabel">|strname|</th>\n' \
                         '</tr>\n')
        keys = lampadasweb.pages.sort_by('code')
        odd_even = OddEven()
        for key in keys:
            page = lampadasweb.pages[key]
            if sessions.session and sessions.session.user.can_edit(page_code=page.code)==1:
                edit_icon = '<a href="|uri.base|page_edit/' + str(page.code) + '|uri.lang_ext|">' + EDIT_ICON_SM + '</a>\n'
            else:
                edit_icon = ''
            if page.section_code > '':
                section_name = lampadasweb.sections[page.section_code].name[uri.lang]
            else:
                section_name = ''

            box.write('<tr class="%s">\n' \
                      '  <td>%s</td>\n' \
                      '  <td>%s</td>\n' \
                      '  <td>%s</td>\n' \
                      '  <td>%s</td>\n' \
                      '  <td><i>%s</i></td>\n' \
                      '</tr>\n' \
                      % (odd_even.get_next(),
                         edit_icon,
                         page.code,
                         page.template_code,
                         section_name,
                         escape_tokens(safestr(page.menu_name[uri.lang]))
                        ))
        box.write('</table>\n')
        return box.get_value()

class TabPage(Table):

    def __init__(self):
        Table.__init__(self, 'page', self.method)

    def method(self, uri):
        if not sessions.session:
            return '|blknopermission|'
        elif sessions.session.user.can_edit(page_code=uri.code)==0:
            return '|blknopermission|'

        if uri.code > '':
            page = lampadasweb.pages[uri.code]
            
            box = WOStringIO('<form method=GET action="|uri.base|data/save/page">\n' \
                             '<table class="box"><tr><th colspan="3">|strpage|: %s</th></tr>\n' \
                             '<input type=hidden name="page_code" value="%s">\n' \
                             '<tr><td class="label">|strsection|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|strtemplate|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|stronly_dynamic|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|stronly_registered|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|stronly_admin|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|stronly_sysadmin|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|strurl_data|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|stradjust_sort_order|</td>\n<td>%s</td>\n<td>%s</td>\n</tr>\n' \
                             '</table>\n' \
                             '</form>\n' % (escape_tokens(page.code),
                                            page.code,
                                            widgets.section_code(page.section_code, uri.lang),
                                            widgets.template_code(page.template_code),
                                            widgets.tf('only_dynamic', page.only_dynamic),
                                            widgets.tf('only_registered', page.only_registered),
                                            widgets.tf('only_admin', page.only_admin),
                                            widgets.tf('only_sysadmin', page.only_sysadmin),
                                            widgets.data(page.data),
                                            widgets.adjust_sort_order(),
                                            widgets.save()))

            # List the available translations
            box.write('<table class="box" style="width:100%"><tr><th colspan="3">|strtranslations|</th></tr>\n')

            odd_even = OddEven()
            for lang in languages.supported_keys(uri.lang):
                if not page.page[lang]==None:
                    box.write('<form method=GET action="|uri.base|data/save/page_lang">\n' \
                              '<input type=hidden name="page_code" value="%s">\n' \
                              '<input type=hidden name="lang" value="%s">\n' \
                              '<tr class="%s"><td class="sectionlabel" colspan="3">%s</td></tr>\n' \
                              '<tr class="%s"><td class="label">|strversion|:</td><td>%s</td>\n<td></td></tr>\n' \
                              '<tr class="%s"><td class="label">|strtitle|:</td><td>%s</td>\n<td></td></tr>\n' \
                              '<tr class="%s"><td class="label">|strmenu_name|:</td><td>%s</td>\n<td></td></tr>\n' \
                              '<tr class="%s"><td class="label">|strpage|:</td><td>%s</td>\n<td>%s</td>\n</tr>\n' \
                              '</form>'
                              % (page.code,
                                 lang,
                                 odd_even.get_next(), languages[lang].name[uri.lang],
                                 odd_even.get_last(), widgets.version(page.version[lang], ''),
                                 odd_even.get_last(), widgets.title(page.title[lang], ''),
                                 odd_even.get_last(), widgets.menu_name(page.menu_name[lang]),
                                 odd_even.get_last(), widgets.page(escape_tokens(page.page[lang])),
                                 widgets.save()))

            # Add a new translation if there are untranslated languages.
            if len(page.untranslated_lang_keys(uri.lang)) > 0:
                box.write('<form method=GET action="|uri.base|data/save/newpage_lang">\n' \
                      '<input type=hidden name="page_code" value="%s">\n' \
                      '<tr class="%s"><td class="sectionlabel" colspan="3">|stradd_translation|</td></tr>' \
                      '<tr class="%s"><td class="label">|strlanguage|:</td><td>%s</td>\n<td></td></tr>\n' \
                      '<tr class="%s"><td class="label">|strversion|:</td><td>%s</td>\n<td></td></tr>\n' \
                      '<tr class="%s"><td class="label">|strtitle|:</td><td>%s</td>\n<td></td></tr>\n' \
                      '<tr class="%s"><td class="label">|strmenu_name|:</td><td>%s</td>\n<td></td></tr>\n' \
                      '<tr class="%s"><td class="label">|strpage|:</td><td>%s</td>\n<td>%s</td>\n</tr>\n' \
                      '</form>'
                      % (page.code,
                         odd_even.get_next(),
                         odd_even.get_last(), widgets.new_page_lang(uri.code, uri.lang),
                         odd_even.get_last(), widgets.version('1.0'),
                         odd_even.get_last(), widgets.title(''),
                         odd_even.get_last(), widgets.menu_name(''),
                         odd_even.get_last(), widgets.page(''),
                         widgets.add()))
            box.write('</table>')
        else:
            page = Page()
            box = WOStringIO('<form method=GET action="|uri.base|data/save/newpage">\n' \
                             '<table class="box"><tr><th colspan="3">|stradd_page|</th></tr>\n' \
                             '<tr><td class="label">|strpage_code|</td>\n<td><input type=text name="page_code"></td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|strsection|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|strtemplate|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|stronly_dynamic|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|stronly_registered|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|stronly_admin|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|stronly_sysadmin|</td>\n<td>%s</td>\n<td></td>\n</tr>\n' \
                             '<tr><td class="label">|strurl_data|</td>\n<td>%s</td>\n<td><input type=submit name="save" value="|strsave|"></td>\n</tr>\n' \
                             '</table>\n' \
                             '</form>\n' % (widgets.section_code(page.section_code, uri.lang),
                                            widgets.template_code(page.template_code),
                                            widgets.tf('only_dynamic', page.only_dynamic),
                                            widgets.tf('only_registered', page.only_registered),
                                            widgets.tf('only_admin', page.only_admin),
                                            widgets.tf('only_sysadmin', page.only_sysadmin),
                                            widgets.data(page.data)))
        return box.get_value()
        
class TabStrings(Table):

    def __init__(self):
        Table.__init__(self, 'strings', self.method)

    def method(self, uri):
        log(3, 'Creating strings table')
        box = WOStringIO('<table class="box" width="100%%">\n' \
                         '<tr><th colspan="3">|strstrings|</th></tr>\n' \
                         '<tr><th class="collabel" colspan="2">|strstring_code|</th>\n' \
                         '    <th class="collabel">|strstring|</th>\n' \
                         '</tr>\n')
        keys = lampadasweb.strings.sort_by('code')
        odd_even = OddEven()
        for key in keys:
            string = lampadasweb.strings[key]
            if sessions.session and sessions.session.user.can_edit(string_code=string.code)==1:
                edit_icon = '<a href="|uri.base|string_edit/' + str(string.code) + '|uri.lang_ext|">' + EDIT_ICON_SM + '</a>\n'
            else:
                edit_icon = ''

            box.write('<tr class="%s">\n' \
                      '  <td>%s</td>\n' \
                      '  <td>%s</td>\n' \
                      '  <td>%s</td>\n' \
                      '</tr>\n' \
                      % (odd_even.get_next(),
                         edit_icon,
                         string.code,
                         escape_tokens(safestr(string.string[uri.lang]))
                        ))
        box.write('</table>\n')
        return box.get_value()

class TabString(Table):

    def __init__(self):
        Table.__init__(self, 'string', self.method)

    def method(self, uri):
        if not sessions.session:
            return '|blknopermission|'
        elif sessions.session.user.can_edit(string_code=uri.code)==0:
            return '|blknopermission|'

        if uri.code > '':
            webstring = lampadasweb.strings[uri.code]

            box = WOStringIO('<form method=GET action="|uri.base|data/save/string">\n' \
                             '<table class="box"><tr><th colspan="2">|strstring|</th></tr>\n' \
                             '<tr><td class="label">|strstring_code|:</td>\n<td>%s</td>\n</tr>\n' \
                             '</table>\n' \
                             '</form>\n' % (webstring.code))

            # List the available translations
            box.write('<table class="box" style="width:100%"><tr><th colspan="3">|strtranslations|</th></tr>\n')

            odd_even = OddEven()
            for lang in languages.supported_keys(uri.lang):
                if not webstring.string[lang]==None:
                    box.write('<form method=GET action="|uri.base|data/save/string_lang">\n' \
                              '<input type=hidden name="string_code" value="%s">\n' \
                              '<input type=hidden name="lang" value="%s">\n' \
                              '<tr class="%s"><td class="sectionlabel" colspan="3">%s</td><td></td></tr>\n' \
                              '<tr class="%s"><td class="label">|strversion|</td><td>%s:</td><td></td>'
                              '<tr class="%s"><td class="label">|strstring|</td><td>%s:</td><td>%s</td>'
                              '</form>'
                              % (webstring.code, lang,
                                 odd_even.get_next(), languages[lang].name[uri.lang],
                                 odd_even.get_last(), widgets.version(webstring.version[lang]),
                                 odd_even.get_last(), widgets.string(webstring.string[lang]),
                                 widgets.save()))

            # Add a new translation if there are untranslated languages.
            if len(webstring.untranslated_lang_keys(uri.lang)) > 0:
                box.write('<form method=GET action="|uri.base|data/save/newstring_lang">\n' \
                          '<input type=hidden name="string_code" value="%s">\n' \
                          '<tr class="%s"><td class="sectionlabel" colspan="3">|stradd_translation|</td></tr>' \
                          '<tr class="%s"><td class="label">|strlanguage|:</td><td>%s</td><td></td></tr>' \
                          '<tr class="%s"><td class="label">|strversion|:</td><td>%s</td><td></td></tr>' \
                          '<tr class="%s"><td class="label">|strstring|:</td><td>%s</td><td>%s</td></tr>'
                          '</form>'
                          % (webstring.code,
                             odd_even.get_next(),
                             odd_even.get_last(), widgets.new_string_lang(uri.code, uri.lang),
                             odd_even.get_last(), widgets.version('1.0'),
                             odd_even.get_last(), widgets.string(''),
                             widgets.save()))
            box.write('</table>')
        else:
            webstring = String()
            box = WOStringIO('<form method=GET action="|uri.base|data/save/newstring">\n' \
                             '<table class="box"><tr><th colspan="3">|stradd_string|</th></tr>\n' \
                             '<tr class="odd"><td class="label">|strstring_code|:</td>\n' \
                             '    <td><input type=text name="string_code" value="%s"></td>\n' \
                             '    <td colspan="2">%s</td>\n' \
                             '</tr>\n' \
                             '</table>\n' \
                             '</form>\n' % (webstring.code, widgets.add()))
            
        return box.get_value()

class TabOMF(Table):
    
    def __init__(self):
        Table.__init__(self, 'omf', self.method)

    def method(self, uri):
        log(3, 'Creating omf table')
        box = WOStringIO('<xml version="1.0" encoding="UTF-8"?>\n')
        box.write('<omf>\n')
        if uri.id > 0:
            box.write(OMF(uri.id).omf)
        else:
            for doc_id in lampadas.docs.sort_by('id'):
                doc = lampadas.docs[doc_id]
                if doc.pub_status_code=='N':
                    box.write(OMF(doc_id).omf + '\n')
        box.write('</omf>\n')
        return box.get_value()

class TabFileMetadata(Table):
    
    def __init__(self):
        Table.__init__(self, 'file_metadata', self.method)

    def method(self, uri):
        log(3, 'Creating file_metadata table')
        if uri.filename > '':
            sourcefile = sourcefiles[uri.filename]
        elif uri.id > 0:
            doc = lampadas.docs[uri.id]
            docfile = doc.find_top_file()
            if docfile==None:
                return ''
            sourcefile = sourcefiles[docfile.filename]
        
        # Read the format_name
        format = lampadas.formats[sourcefile.format_code]
        if format:
            format_name = format.name[uri.lang]
        else:
            format_name = ''

        # Read the dtd_name
        dtd = lampadas.dtds[sourcefile.dtd_code]
        if dtd:
            dtd_name = dtd.name[uri.lang]
        else:
            dtd_name = ''
        box = WOStringIO('<table class="box"><tr><th colspan="2">%s |strmetadata|</th></tr>\n'
                         '<tr><td class="label">|strformat|:</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strdtd|:</td><td>%s %s</td></tr>\n'
                         '<tr><td class="label">|strtitle|:</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strabstract|:</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strversion|:</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strpub_date|:</td><td>%s</td></tr>\n'
                         '<tr><td class="label">|strisbn|:</td><td>%s</td></tr>\n'
                         '</table>\n'
                         % (sourcefile.filename,
                            format_name,
                            dtd_name,
                            sourcefile.dtd_version,
                            sourcefile.title,
                            sourcefile.abstract,
                            sourcefile.version,
                            sourcefile.pub_date,
                            sourcefile.isbn))
        return box.get_value()

class TabEditThisPage(Table):
    
    def __init__(self):
        Table.__init__(self, 'edit_this_page', self.method)

    def method(self, uri):
        log(3, 'Creating edit_this_page table')
        if not sessions.session:
            return ''
        elif sessions.session.user.can_edit(page_code=uri.page_code)==0:
            return ''
        if uri.page_code=='page_edit':
            return '<center><a href="|uri.base||uri.code||uri.lang_ext|">|strview_this_page|</a></center>'
        else:
            return '<center><a href="|uri.base|page_edit/|uri.page_code||uri.lang_ext|">|stredit_this_page|</a></center>'

class TabDocLangStats(Table):

    def __init__(self):
        Table.__init__(self, 'doc_lang_stats', self.method)

    def method(self, uri):
        log(3, 'Creating doc_lang_stats table')
        box = WOStringIO('<table class="box">\n' \
                         '<tr><th colspan="3">|strdoc_lang_stats|</th></tr>\n' \
                         '<tr><th class="collabel">|strlanguage|</th>\n' \
                             '<th class="collabel" align="right">|strcount|</th>\n' \
                             '<th class="collabel" align="right">|strpct|</th>\n' \
                         '</tr>\n')
        stattable = stats['doc_lang']
        odd_even = OddEven()
        for key in languages.sort_by_lang('name', uri.lang):
            stat = stattable[key]
            if stat==None: continue
            box.write('<tr class="%s"><td class="label">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                          '<td align="right">%s</td>\n' \
                      '</tr>\n'
                      % (odd_even.get_next(), languages[stat.label].name[uri.lang], stat.value, fpformat.fix(stattable.pct(key) * 100, 2)))
        box.write('<tr class="%s"><td class="label">|strtotal|</td>\n' \
                      '<td align="right">%s</td><td></td>\n' \
                  '</tr></table>'
                  % (odd_even.get_next(), stattable.sum()))
        return box.get_value()
        
class TableMap(LampadasCollection):

    def __init__(self):
        self.data = {}
        self['tabdocs'] = DocTable()
        self['tabdocs_expanded'] = DocTableExpanded()
        self['tabdocadmin'] = DocAdmin()
        self['tabrecentnews'] = TabNews(items=10)
        self['tabnews'] = TabNews()
        self['tabnewsitem'] = TabNewsItem()
        self['tabpages'] = TabPages()
        self['tabpage'] = TabPage()
        self['tabstrings'] = TabStrings()
        self['tabstring'] = TabString()
        self['tabomf'] = TabOMF()
        self['tabfile_metadata'] = TabFileMetadata()
        self['tabedit_this_page'] = TabEditThisPage()
        self['tabdoc_lang_stats'] = TabDocLangStats()

tables = Tables()
tablemap = TableMap()

