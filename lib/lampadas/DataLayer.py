#!/usr/bin/python

"""
Lampadas system

This modules defines Data Objects (Users, Documents, Notes, Topics, etc.)
and a Database object that manages SQL queries to the back-end and acts as
a data object factory.
"""

### THIS CODE IS NOT FUNCTIONAL YET ###

__version__ = '0.2'


# Modules #####################################################################

from types import StringType


# BaseConfig ##################################################################

class ConfigFileReadErrorException(Exception) :
	pass

class ConfigFile :
	"""
	Basic configuration options (dbname, dbtype), used to know where we can find
	the database.
	"""

	def __init__(self) :
		import ConfigParser

		self.config = ConfigParser.ConfigParser()
		self.config.readfp(open('lampadas.conf'))
		self.parse()

	def parse(self) :
		if not self.config.has_section('DB') :
			raise ConfigFileReadErrorException("File 'lampadas.conf' is missing or does not contain a '[DB]' section")
			
		if not self.config.has_option('DB', 'dbtype') :
			raise ConfigFileReadErrorException("Can't read option 'dbtype' from lampadas.conf")
		self.dbtype = self.config.get('DB', 'dbtype')
		
		if not self.config.has_option('DB', 'dbname') :
			raise ConfigFileReadErrorException("Can't read option 'dbname' from lampadas.conf")
		self.dbname = self.config.get('DB', 'dbname')
		

# User ########################################################################

class User :
	"""
	A user is known by the system and can login to manipulate documents
	and act on the database according to his rights.
	"""

	def __init__(self) :
		self.username = ""
		self.user_id = ""
		self.firstname = ""
		self.surname = ""
		self.name = "%s %s" % (self.firstname, self.surname)
		self.email = ""
		self.maintainer_id = ""
		self.editor_id = ""
		self.is_admin = 0

	def get_documents(self) :
		"""
		Return list of documents. Document list factory.
		"""
		# SELECT d.doc_id, d.title, d.class, d.pub_status, d.url, ps.pub_status_name, du.role, du.active, du.email FROM document d, document_user du, pub_status ps WHERE d.doc_id=du.doc_id AND d.pub_status = ps.pub_status AND user_id=$user_id
		pass

	def get_notes(self) :
		"""
		Return list of notes. notes list factory.
		"""
		# SELECT un.date_entered, un.notes, u.username FROM username u, username_notes un WHERE u.user_id = un.user_id AND u.user_id = $user_id
		pass

	def add_note(self) :
		"""
		Add a new note
		"""
	# INSERT INTO username (user_id, notes, creator_id) VALUES ($user_id, " . wsq($notes) . ", " . CurrentUserID() . ")
		pass

	def is_maintainer(self) :
		"""
		Return true if user is a maintainer or an admin
		"""
		# SELECT COUNT(*) FROM document_user WHERE active='t' AND user_id=" . self.user_id
		return self.is_admin or XYZ


# Document ####################################################################

class Document :
	"""
	A document is stored in the system to be collaboratively written,
	edited, proof-read and maintained. The system will also publish it.
	"""

	def __init__(self) :
		self.doc_id = None
		self.title = None
		self.filename = None
		self.type = None                   ## Modified (was self.class)
		self.format = None
		self.dtd = (dtd_name, dtd_version)
		self.version = None
		self.last_update = None
		self.url = None
		self.isbn = None
		self.pub_status = None
		self.author_status = None
		self.review_status = None
		self.tickle_date = None
		self.pub_date = None
		self.ref_url = None
		self.tech_review_status = None
		self.maintained = 0
		self.license_id = 0
		self.license = None
		self.abstract = None
		self.wiki = None
		self.rating = None

	# topics ###
	
	def get_users(self) :
		"""
		Return list of users with their roles
		"""
		# "SELECT document_user.user_id, role, document_user.email, active, username, first_name, middle_name, surname FROM document_user, username WHERE document_user.user_id = username.user_id AND doc_id=$doc_id"
		pass

	# topics ###
	
	def get_topics(self) :
		"""
		Return a list of topics
		"""
		# SELECT dt.topic_num, dt.subtopic_num, t.topic_name, s.subtopic_name FROM topic t, subtopic s, document_topic dt WHERE t.topic_num = s.topic_num AND dt.topic_num = s.topic_num AND dt.subtopic_num = s.subtopic_num AND dt.doc_id = $doc_id
		pass

	# notes ###
	
	def get_notes(self) :
		"""
		Return a list of notes
		"""
		# "SELECT n.date_entered, n.notes, u.username FROM notes n, username u WHERE n.creator_id = u.user_id AND n.doc_id = $doc_id ORDER BY n.date_entered"
		pass

	# revisions ###
	
	def get_revisions(self) :
		"""
		Return a list of revisions
		"""
		#
		pass

	def add_revision(self, revision) :
		"""
		Add a new revision
		"""
		# Turn revision into an INSERT
	# INSERT INTO document_rev(doc_id, rev_id, version, pub_date, initials, notes) VALUES ($doc_id, $rev_id, $version, " . &wsq($pub_date) . ", " . &wsq($initials) . ", " . &wsq($notes) . ")
		pass

	def update_revision(self, revision) :
		"""
		Update an existing revision
		"""
		# doc_id, rev_id, version, pub_date, initials, notes) :
	# UPDATE document_rev SET version=" . wsq($version) . ", pub_date=" . wsq($pub_date) . ", initials=" . wsq($initials) . ", notes=" . wsq($notes) . " WHERE doc_id=$doc_id AND rev_id=$rev_id"
		pass

	def remove_revision(self, revision) :
		"""
		Remove a document revision
		"""
	# DELETE FROM document_rev WHERE doc_id=$doc_id AND rev_id=$rev_id
		pass

# Note ####################################################################

class Note :
	"""
	A note is written by a user and attached to a document
	"""

	def __init__(self) :
		self.document = None
		self.date = None
		self.text = None
		self.user = None

# Topic ####################################################################

class Topic :
	"""
	A topic tells what a document is about
	"""

	def __init__(self) :
		self.num = None
		self.name = None
		self.description = None
		self.subtopic_num = None
		self.subtopic_name = None

# Revision ####################################################################

class Revision :
	"""
	A revision describes a document version
	"""

	def __init__(self) :
		self.version = None
		self.pub_date = None
		self.initials = None
		self.notes = None

# Role ####################################################################

class Role :
	"""
	A role that can be taken by a user
	"""

	def __init__(self,name) :
		self.name = name

# Role ####################################################################

class License :
	"""
	A license for a document
	"""

	def __init__(self,name) :
		self.name = name

# Role ####################################################################

class Format :
	"""
	A document format
	"""

	def __init__(self, name, long_name) :
		self.name = name
		self.long_name = long_name

# Role ####################################################################

class DTD :
	"""
	A Document Type Definition
	"""

	def __init__(self,name) :
		self.name = name

# DocClass ####################################################################

class DocClass :
	"""
	The class of a document (HOWTO, Guide, FAQ, etc.)
	"""

	def __init__(self) :
		self.name = name
		self.long_name = long_name

# PubStatus ####################################################################

class PubStatus :
	"""
	The publication status of a document (Wishlist, pending, active, etc.)
	"""

	def __init__(self) :
		self.code = None
		self.name = None
		self.description = None

# ReviewStatus ################################################################

class PubStatus :
	"""
	The review status of a document (in progress, reviewed, etc.)
	"""

	def __init__(self) :
		self.code = None
		self.name = None


# main
if __name__ == '__main__' :
	print "This should start the unit tests"


# Database ###############################################################

class UnknownDBException(Exception) :
	pass

def get_database(dbtype = '', dbname = '') :
	"""
	To let people use different DBs, use specific class derived from Database
	"""

	# Use config file
	dbconfig = ConfigFile()

	# Overwrite options if arguments specified
	if dbtype != '' :
		dbconfig.dbtype = dbtype
	if dbname != '' :
		dbconfig.dbname = dbname

	if dbconfig.dbtype == 'pgsql' :
		return PgSQLDatabase(dbconfig.dbname)
	elif dbconfig.dbtype == 'mysql' :
		return MySQLDatabase(dbconfig.dbname)
	else :
		raise UnknownDBException('Unknown database type %s' % dbconfig.dbtype)

class Database :
	"""
	The database contains all users and documents
	"""
	
	def __init__(self,dbname) :
		"""
		Init database connection
		"""
		self.dbname = None

	def get_config(self, name) :
		"""
		Return value of config parameter
		"""
		cur = self.connection.cursor()
		cur.execute("SELECT value FROM config WHERE name = %s", name)
		tmp = cur.fetchone()
		return tmp[0]

	# users ###
	
	def mk_user(self, row) :
		"""
		User factory (takes a single row query result as argument)
		"""
		u = User()
		
		u.user_id = row[0]
		u.username = row[1].rstrip()
		
		if isinstance(row[3], StringType):
			u.firstname = row[3].rstrip()
			
		if isinstance(row[4], StringType):
			u.surname = row[4].rstrip()

		if isinstance(row[5], StringType):
			u.name = row[5].rstrip()

		if isinstance(row[6], StringType):
			u.email = row[6].rstrip()

		u.maintainer_id = 0  # XXX FIXME
		u.editor_id = 0  # XXX FIXME
		u.is_admin = row[7]
		return u
	
	def get_user_by_name(self,username) :
		"""
		Return user by username entry
		"""
		cur = self.connection.cursor()
		cur.execute('SELECT * from username WHERE username = %s', username)
		return self.mk_user(cur.fetchone())
	
	def get_user_by_id(self,user_id) :
		"""
		Return user by user_id entry
		"""
		cur = self.connection.cursor()
		cur.execute('SELECT * from username WHERE user_id = %s', user_id)
		return self.mk_user(cur.fetchone())

	def get_users(self) :
		"""
		Return the list of all users. User list Factory.
		"""
		cur = self.connection.cursor()
		cur.execute("SELECT * from username")
		return [self.mk_user(row) for row in cur.fetchall()]
	
	def get_user_from_sessionid(self,session_id) :
		"""
		Return a user that has corresponding session id

		XXXFIXME: how easy is it to steal a session ?
		"""
		#$session_id = $CGI->cookie('lampadas_session')
		#$currentuser_id = $DB->Value("SELECT user_id FROM username WHERE session_id='$session_id'")
		#if ($currentuser_id) {
		#	%currentuser = User($foo, $currentuser_id)
		pass

	# documents ###
	
	def get_document(self,doc_id) :
		"""
		Document factory
		"""
		# SELECT doc_id, title, class, format, dtd, dtd_version, version, last_update, url, isbn, pub_status, review_status, tickle_date, pub_date, ref_url, tech_review_status, maintained, license, abstract, rating FROM document WHERE doc_id=$doc_id
		return Document()

	def add_document(self,doc) :
		"""
		Add a new document
		"""
		# turn Document instance into SQL INSERT
		pass

	def update_document(self, doc) :
		"""
		Update document description
		"""
		# turn Document instance into SQL UPDATE
		pass

	def doc_count(self,type=None) :
		"""
		return number of documents
		"""
		if type == 'byClass' :
			# SELECT COUNT(*) FROM document WHERE class IN (" . $class . ")")	# SELECT COUNT(*) FROM document
			pass
		elif type == 'byPubStatus' :
			# SELECT COUNT(*) FROM document WHERE pub_status in (" . $pub_status . ")")
			pass
		else :
			# SELECT COUNT(*) FROM document
			pass

	# topics ###
	
	def get_topic(self, topic_num) :
		"""
		Return the topic
		"""
		# SELECT topic_num, topic_name, topic_description FROM topic WHERE topic_num=$topic_num
		pass

	def get_topics(self) :
		"""
		Return list of topics
		"""
		# SELECT topic_num, topic_name, topic_description FROM topic
		pass

	def SaveTopic(self, topic_num, topic_name, topic_description) :
		"""
		Save a given topic
		"""
		# UPDATE topic SET topic_name=" . wsq($topic_name) . ", topic_description=" . wsq($topic_description) . " WHERE topic_num=$topic_num
		pass

	def Subtopics(self, topic_num) :
		"""
		Return the subtopics of a given topic
		"""
		"""
	my %subtopics = ()
	my $sql = "SELECT topic.topic_num, topic_name, topic_description, subtopic_num, subtopic_name, subtopic_description from subtopic, topic WHERE subtopic.topic_num = topic.topic_num"
	$sql .= " AND topic.topic_num = $topic_num" if ($topic_num)
	my $recordset = $DB->Recordset($sql)
	while (@row = $recordset->fetchrow) {
		$topicnum	= strip($row[0])
		$topicname	= strip($row[1])
		$topicdesc	= strip($row[2])
		$subtopicnum	= strip($row[3])
		$subtopicname	= strip($row[4])
		$subtopicdesc	= strip($row[5])
		$key		= $topicnum . '.' . $subtopicnum
		$subtopics{$key}{topicnum}	= $topicnum
		$subtopics{$key}{topicname}	= $topicname
		$subtopics{$key}{topicdesc}	= $topicdesc
		$subtopics{$key}{num}		= $subtopicnum
		$subtopics{$key}{name}		= $subtopicname
		$subtopics{$key}{description}	= $subtopicdesc
	}
	return %subtopics
	"""
		pass

	def SaveSubtopic(self, topic_num, subtopic_num,
				 subtopic_name, subtopic_description) :
		"""
		$DB->Exec("UPDATE subtopic SET subtopic_name=" . wsq($subtopic_name) . ", subtopic_description=" . wsq($subtopic_description) . " WHERE topic_num=$topic_num AND subtopic_num=$subtopic_num")
	}"""
		pass
  
	# roles ###
	
	def get_roles(self) :
		"""
		Return list of roles
		"""
		# SELECT role FROM role
		pass

	# licenses ###
	
	def get_licenses(self) :
		"""
		Return list of licenses
		"""
		# SELECT license FROM license
		pass

	# formats ###
	
	def get_formats(self) :
		"""
		Return list of formats
		"""
		# SELECT format, format_name FROM format"
		pass

	# dtds ###
	
	def get_dtds(self) :
		"""
		Return list of dtds
		"""
		# SELECT dtd FROM dtd"
		pass


try:
	import pyPgSQL
	
	class PgSQLDatabase(Database) :

		def __init__(self,dbname) :
			from pyPgSQL import PgSQL
			self.connection = PgSQL.connect(database=dbname)
except ImportError:
	# PostgresSQL back-end is not available
	pass

try:
	import pyMySQL

	class MySQLDatabase(Database) :

		def __init__(self,dbname) :
			from pyMySQL import MySQL
			self.cnx = MySQL.connection(dbname=dbname)

except ImportError:
	# MySQL back-end is not available
	pass
