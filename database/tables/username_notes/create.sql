CREATE TABLE username_notes
(
	username		CHAR(40)	NOT NULL	REFERENCES username(username),
	notes			TEXT,
	creator			CHAR(40)	NOT NULL	REFERENCES username(username),
	created			TIMESTAMP	NOT NULL	DEFAULT now(),
	updated			TIMESTAMP	NOT NULL	DEFAULT now(),

	PRIMARY KEY (username, created)
);
