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
from Log import log
from mod_python import apache
import smtplib
import string
import whrandom

def document(req, doc_id, title, url, ref_url, pub_status_code, class_id,
             review_status_code, tech_review_status_code, license, pub_date,
             last_update, version, tickle_date, isbn, lang, abstract):

    if not doc_id:
        return error("A required parameter is missing. Please go back and correct the error.")

    doc = lampadas.Docs[int(doc_id)]
    if doc == None:
        return error("Cannot find document " + str(doc_id))

    doc.Title                   = title
    doc.URL                     = url
    doc.HomeURL                 = ref_url
    doc.PubStatusCode           = pub_status_code
    doc.ClassID                 = int(class_id)
    doc.ReviewStatusCode        = review_status_code
    doc.TechReviewStatusCode    = tech_review_status_code
    doc.License                 = license
    doc.PubDate                 = pub_date
    doc.LastUpdate              = last_update
    doc.Version                 = version
    doc.TickleDate              = tickle_date
    doc.ISBN                    = isbn
    doc.Lang                    = lang
    doc.Abstract                = abstract
    doc.Save()
    referer = req.headers_in['referer']
    req.headers_out['location'] = referer
    req.status = apache.HTTP_MOVED_TEMPORARILY
    return

def user(req, username, email, first_name, middle_name, surname):
    user = lampadas.users[username]
    if not user == None:
        user.email = email
        user.first_name = first_name
        user.middle_name = middle_name
        user.surname = surname
        user.save()

def newuser(req, username, email, first_name, middle_name, surname):
    
    if username == '':
        return page_factory.page('username_required')

    user = lampadas.users[username]
    if user.username>'':
        return page_factory.page('user_exists')
    if lampadas.users.is_email_taken(email):
        return page_factory.page('email_exists')

    # establish random password, 10 characters
    # 
    chars = string.letters + string.digits
    password = ''
    for x in range(10):
        password += whrandom.choice(chars)

    lampadas.users.add(username, first_name, middle_name, surname, email, 'f', 'f', password, '', 'default')

    # mail the password to the new user
    # 
    server = smtplib.SMTP(config.smtp_server)
    server.set_debuglevel(1)
    server.sendmail(config.admin_email, email, 'Your password is ' + password)
    server.quit()
    return page_factory.page('account_created')

def error(message):
    return message

