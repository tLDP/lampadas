DROP TABLE pub_status;

CREATE TABLE pub_status
(
	pub_status		CHAR		NOT NULL,
	pub_status_name		TEXT,
	pub_status_desc		TEXT,
	
	PRIMARY KEY (pub_status)
);
