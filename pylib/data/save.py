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

from Config import config
from DataLayer import lampadas
from HTML import page_factory
from Lintadas import lintadas
from Log import log
from mod_python import apache
import smtplib
import string
import whrandom

def newdocument(req, username, doc_id, title, url, ref_url, pub_status_code, type_code,
             review_status_code, tech_review_status_code, maintainer_wanted,
             license_code, pub_date, last_update, version, tickle_date, isbn,
             format_code, dtd_code, dtd_version, lang, abstract):

    newdoc_id = lampadas.docs.add(title, type_code, format_code, dtd_code,
            dtd_version, version, last_update, url, isbn,
            pub_status_code, review_status_code, tickle_date, pub_date,
            ref_url, tech_review_status_code, license_code, abstract, lang, '')

    # Add the current user as the author of the document
    doc = lampadas.docs[newdoc_id]
    doc.users.add(username)
    
    lintadas.check(newdoc_id)

    redirect(req, '/editdoc/' + str(newdoc_id))

def document(req, username, doc_id, title, url, ref_url, pub_status_code, type_code,
             review_status_code, tech_review_status_code, maintainer_wanted,
             license_code, pub_date, last_update, version, tickle_date, isbn,
             format_code, dtd_code, dtd_version, lang, abstract):

    if not doc_id:
        return error("A required parameter is missing. Please go back and correct the error.")

    doc = lampadas.docs[int(doc_id)]
    if doc==None:
        return error("Cannot find document " + str(doc_id))

    doc.title                   = title
    doc.url                     = url
    doc.home_url                = ref_url
    doc.pub_status_code         = pub_status_code
    doc.type_code               = type_code
    doc.review_status_code      = review_status_code
    doc.tech_review_status_code = tech_review_status_code
    doc.maintainer_wanted       = int(maintainer_wanted)
    doc.license_code            = license_code
    doc.pub_date                = pub_date
    doc.last_update             = last_update
    doc.version                 = version
    doc.tickle_date             = tickle_date
    doc.ibsn                    = isbn
    doc.format_code             = format_code
    doc.dtd_code                = dtd_code
    doc.dtd_version             = dtd_version
    doc.lang                    = lang
    doc.abstract                = abstract
    doc.save()
    lintadas.check(int(doc_id))
    go_back(req)

def newdocument_user(req, doc_id, username, active, role_code, email, action):
    user = lampadas.users[username]
    if user==None or user.username<>username:
        return error('User not found.')
    else:
        doc = lampadas.docs[int(doc_id)]
        doc.users.add(username, role_code, email, int(active))
        lintadas.check(doc.id)
        go_back(req)
    
def document_user(req, doc_id, username, active, role_code, email, action, delete=''):
    doc = lampadas.docs[int(doc_id)]
    if delete=='on':
        doc.users.delete(username)
        lintadas.check(doc.id)
        go_back(req)
    else:
        docuser = doc.users[username]
        docuser.active = int(active)
        docuser.role_code = role_code
        docuser.email = email
        docuser.save()
        lintadas.check(doc.id)
        go_back(req)
    
def newdocument_file(req, doc_id, filename, top, format_code, action):
    doc = lampadas.docs[int(doc_id)]
    doc.files.add(doc_id, filename, int(top), format_code)
    lintadas.check(int(doc_id))
    go_back(req)
    
def document_file(req, doc_id, filename, top, format_code, action, delete=''):
    doc = lampadas.docs[int(doc_id)]
    if delete=='on':
        doc.files.delete(filename)
        lintadas.check(int(doc_id))
        go_back(req)
    else:
        file = doc.files[filename]
        file.top = int(top)
        file.format_code = format_code
        file.save()
        lintadas.check(int(doc_id))
        go_back(req)
    
def newdocument_version(req, doc_id, version, pub_date, initials, notes, action):
    doc = lampadas.docs[int(doc_id)]
    doc.versions.add(version, pub_date, initials, notes)
    lintadas.check(int(doc_id))
    go_back(req)
    
def document_version(req, rev_id, doc_id, version, pub_date, initials, notes, action, delete=''):
    doc = lampadas.docs[int(doc_id)]
    if delete=='on':
        doc.versions.delete(int(rev_id))
        go_back(req)
    else:
        docversion = doc.versions[int(rev_id)]
        docversion.version = version
        docversion.pub_date = pub_date
        docversion.initials = initials
        docversion.notes = notes
        docversion.save()
        go_back(req)
    
def newdocument_topic(req, doc_id, subtopic_code):
    doc = lampadas.docs[int(doc_id)]
    doc.topics.add(subtopic_code)
    go_back(req)
    
def deldocument_topic(req, doc_id, subtopic_code):
    doc = lampadas.docs[int(doc_id)]
    doc.topics.delete(subtopic_code)
    go_back(req)

def newdocument_note(req, doc_id, notes, creator):
    doc = lampadas.docs[int(doc_id)]
    doc.notes.add(notes, creator)
    go_back(req)
    
def newaccount(req, username, email, first_name, middle_name, surname):
    """
    This routine is for when a user requests an account.
    """
    
    if username=='':
        return page_factory.page('username_required')

    user = lampadas.users[username]
    if user:
        return page_factory.page('user_exists')
    if lampadas.users.is_email_taken(email):
        return page_factory.page('email_exists')

    password = random_password()
    mail_password(email, password)
    lampadas.users.add(username, first_name, middle_name, surname, email, 0, 0, password, '', 'default')
    return page_factory.page('account_created')

def random_password():
    """
    Establishes a random password, 10 characters long.
    """
    
    chars = string.letters + string.digits
    password = ''
    for x in range(10):
        password += whrandom.choice(chars)

def mail_password(email, password):
    """
    Mails the password to the user.
    """

    server = smtplib.SMTP(config.smtp_server)
    server.set_debuglevel(1)
    server.sendmail(config.admin_email, email, 'Your password is ' + password)
    server.quit()

def newuser(req, username, email, first_name, middle_name, surname, stylesheet, password, admin, sysadmin, notes):
    """
    This routine is for when an administrator manually adds an account.
    """

    if username=='':
        return page_factory.page('username_required')

    user = lampadas.users[username]
    if user:
        return page_factory.page('user_exists')
    if lampadas.users.is_email_taken(email):
        return page_factory.page('email_exists')

    lampadas.users.add(username, first_name, middle_name, surname, email, int(admin), int(sysadmin), password, notes, stylesheet)
    redirect(req, '/user/' + username)

def user(req, username, first_name, middle_name, surname, email, stylesheet, password, admin, sysadmin, notes):
    user = lampadas.users[username]
    if not user==None:
        user.first_name = first_name
        user.middle_name = middle_name
        user.surname = surname
        user.email = email
        user.stylesheet = stylesheet
        if password > '':
            user.password = password
        user.admin = int(admin)
        user.sysadmin = int(sysadmin)
        user.notes = notes
        user.save()
    referer = req.headers_in['referer']
    req.headers_out['location'] = referer
    req.status = apache.HTTP_MOVED_TEMPORARILY

def error(message):
    return message

def redirect(req, url):
    req.headers_out['location'] = url
    req.status = apache.HTTP_MOVED_TEMPORARILY

def go_back(req):
    referer = req.headers_in['referer']
    req.headers_out['location'] = referer
    req.status = apache.HTTP_MOVED_TEMPORARILY

