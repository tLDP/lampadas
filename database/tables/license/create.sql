CREATE TABLE license
(
	license_code		CHAR(12)	NOT NULL,
	free			BOOLEAN		NOT NULL	DEFAULT False,
	dfsg_free		BOOLEAN		NOT NULL	DEFAULT False,
	osi_cert_free		BOOLEAN		NOT NULL	DEFAULT False,
	url			TEXT,
	sort_order		INT4		NOT NULL,
	created			TIMESTAMP	NOT NULL DEFAULT now(),
	updated			TIMESTAMP	NOT NULL DEFAULT now(),

	PRIMARY KEY (license_code)
);

CREATE INDEX license_upd_idx ON license (updated);
CREATE INDEX license_ctd_idx ON license (created);
