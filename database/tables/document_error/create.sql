CREATE TABLE document_error
(
	doc_id			INT4		NOT NULL	REFERENCES document(doc_id),
	err_id			INT4		NOT NULL	REFERENCES error(err_id),
	notes			TEXT,
	created			TIMESTAMP	NOT NULL DEFAULT now(),
	updated			TIMESTAMP	NOT NULL DEFAULT now(),
	
	PRIMARY KEY (doc_id, err_id)
);
