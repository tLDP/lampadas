CREATE TABLE topic_i18n
(
	topic_code		CHAR(20)	NOT NULL	REFERENCES topic(topic_code),
	lang			CHAR(2)		NOT NULL	REFERENCES language(lang_code),
	topic_name		TEXT		NOT NULL, 
	topic_desc		TEXT,
	created			TIMESTAMP	NOT NULL	DEFAULT now(),
	updated			TIMESTAMP	NOT NULL	DEFAULT now(),

	PRIMARY KEY (topic_code, lang)
);
