#!/usr/bin/python

import os				# Import required modules
import sys
import stat
import string
import commands
import StringIO
import shutil
import StringIO

import BaseHTTPServer

from Log import Log
from HTML import PageFactory
from Globals import VERSION
import Config
from URLParse import URI

Log = Log()
Config = Config.Config()
P = PageFactory()

BaseClass = BaseHTTPServer.BaseHTTPRequestHandler

class RequestHandler(BaseClass):
	"""
	Intercepts the HTTP requests and serves them.
	"""
	def do_GET(self):
		fd = self.send_head()
		if fd:
			shutil.copyfileobj(fd, self.wfile)
			fd.close
	
	def do_HEAD(self):
		fd = self.send_head()
		fd.close()
	
	def send_head(self):
		"""
		Send the requested page.
		"""
		uri = URI(self.path)
		filename = Config.FileDir + uri.Path + uri.Filename
		filename = filename.replace('//','/')
		Log.Write(3, 'looking for file ' + filename)
		
		if os.path.isfile(filename):
			return self.send_File(filename)

		Log.Write(3, 'Sending dynamic page')
		return self.send_HTML(P.Page(self.path, 'EN'))

	def send_HTML(self, HTML):
		"""
		Send the passed HTML page.
		"""
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.send_header("Content-length", len(HTML))
		self.end_headers()
		return StringIO.StringIO(HTML)
		
	def send_File(self, filename):
		"""
		Send the requested file.
		"""
		Log.Write(3, 'Sending file ' + filename)
		temp = string.split(filename, ".")
		if len(temp) > 1:
			fileext = temp[1]
		else:
			if os.path.isfile(filename + ".png"):
				fileext = "png"
			elif os.path.isfile(filename + ".jpeg"):
				fileext = "jpeg"
			if os.path.isfile(filename + ".jpg"):
				fileext = "jpg"
			if os.path.isfile(filename + ".gif"):
				fileext = "gif"
			if fileext:
				filename += "." + fileext

		# Determine mimetype from extension
		if fileext == "html" or fileext == "htm":
			mimetype = "text/html"
		elif fileext == "png":
			mimetype = "image/png"
		elif fileext == "gif":
			mimetype = "image/gif"
		elif fileext == "jpg" or fileext == "jpeg":
			mimetype = "image/jpeg"
		elif fileext == "css":
			mimetype = "text/css"
		else:
			mimetype = "text/plain"

		fd = open(filename, 'r')
		filesize = os.fstat(fd.fileno())[stat.ST_SIZE]
		self.send_response(200)
		self.send_header("Content-type", mimetype)
		self.send_header("Content-length", filesize)
		self.end_headers()
		return fd

	def send_Text(self, text):
		"""
		Send a text message.
		"""
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.send_header("Content-length", len(text))
		self.end_headers()
		return StringIO.StringIO(text)


def WebServer():
	"""
	Initialize the server.
	"""
	interface = Config.Interface
	port = Config.Port

	print "Lampadas " + VERSION + " -- development version!"
	if interface != '':
		print '(Listening on interface %s, port %s)' % (interface, port)
	else:
		print '(Listening on all interfaces, port %s)' % port
	server = BaseHTTPServer.HTTPServer((interface, port), RequestHandler)
	server.serve_forever()


if __name__ == '__main__':
	WebServer()

