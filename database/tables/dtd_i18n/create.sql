CREATE TABLE dtd_i18n
(
	dtd_code		CHAR(12)	NOT NULL	REFERENCES dtd(dtd_code),
	lang			CHAR(2)		NOT NULL	REFERENCES language(lang_code),
	dtd_name		TEXT		NOT NULL,
	dtd_desc		TEXT,

	PRIMARY KEY (dtd_code, lang)
);
