CREATE TABLE page_i18n
(
	page_code	CHAR(20)	NOT NULL	REFERENCES page(page_code),
	lang		CHAR(2)		NOT NULL	REFERENCES language(isocode),
	title		TEXT		NOT NULL,
	menu_name	TEXT		NOT NULL,
	page		TEXT		NOT NULL,

	PRIMARY KEY (page_code, lang)
);
