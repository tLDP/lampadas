ALTER TABLE document_user	ADD CONSTRAINT doc_id_fk		FOREIGN KEY (doc_id)			REFERENCES document(doc_id);
ALTER TABLE document_user	ADD CONSTRAINT user_id_fk		FOREIGN KEY (user_id)			REFERENCES username(user_id);
ALTER TABLE document_user	ADD CONSTRAINT role_fk			FOREIGN KEY (role)			REFERENCES role(role);