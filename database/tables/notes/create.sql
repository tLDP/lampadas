CREATE TABLE notes (
	doc_id		INT4		NOT NULL
			REFERENCES document(doc_id),
	date_entered	TIMESTAMP	NOT NULL DEFAULT now(),
	notes		TEXT,
	creator_id	INT4		NOT NULL
			REFERENCES username(user_id),

	PRIMARY KEY (doc_id, date_entered)
);
