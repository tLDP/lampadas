DROP TABLE username;

CREATE TABLE username (
	username	TEXT	NOT NULL,
	first_name	CHAR(20),
	surname		CHAR(20),
	maintainer_id	INT4,
	email		TEXT,
	admin		BOOLEAN,
	editor_id	INT4,

	PRIMARY KEY (username)
);

GRANT ALL ON username TO "www-data";
GRANT SELECT ON username TO root;
