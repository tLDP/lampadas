CREATE TABLE subtopic
(
	topic_num		INT4		NOT NULL,
	subtopic_num		INT4		NOT NULL,
	subtopic_name		TEXT		NOT NULL,
	subtopic_description	TEXT,	

	PRIMARY KEY (topic_num, subtopic_num)
);
