DROP TABLE role;

CREATE TABLE role(
	role		CHAR(12)	NOT NULL,

	PRIMARY KEY (role)
);

GRANT SELECT ON role TO "www-data";

