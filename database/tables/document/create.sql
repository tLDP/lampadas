CREATE TABLE document
(
	doc_id			INT4		NOT NULL,
	lang			CHAR(2)		NOT NULL	REFERENCES language(lang_code),
	title			TEXT,
	short_title		TEXT,
	type_code		CHAR(20)			REFERENCES type(type_code),
	format_code		CHAR(20)			REFERENCES format(format_code),
	dtd_code		CHAR(12)			REFERENCES dtd(dtd_code),
	dtd_version		CHAR(12),
	version			CHAR(12),
	last_update		DATE,
	URL			TEXT,
	ISBN			TEXT,
	pub_status		CHAR				REFERENCES pub_status(pub_status),
	review_status		CHAR				REFERENCES review_status(review_status),
	tickle_date		DATE,
	pub_date		DATE,
	ref_url			TEXT,
	tech_review_status	CHAR				REFERENCES review_status(review_status),
	maintained		BOOLEAN		DEFAULT False,
	maintainer_wanted	BOOLEAN		DEFAULT False,
	license_code		CHAR(12)			REFERENCES license(license_code),
	license_version		CHAR(12),
	copyright_holder	TEXT,
	abstract		TEXT,
	short_desc		TEXT,
	rating			REAL,
	sk_seriesid		CHAR(36),
	replaced_by_id		INT4,

	PRIMARY KEY (doc_id)
);
