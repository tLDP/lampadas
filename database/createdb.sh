#~/bin/bash

psql lampadas -qf audience.sql
psql lampadas -qf class.sql
psql lampadas -qf class_i18n.sql
psql lampadas -qf config.sql
psql lampadas -qf document.sql
psql lampadas -qf document_audience.sql
psql lampadas -qf document_error.sql
psql lampadas -qf document_file.sql
psql lampadas -qf document_rev.sql
psql lampadas -qf document_topic.sql
psql lampadas -qf document_user.sql
psql lampadas -qf document_wiki.sql
psql lampadas -qf doc_vote.sql
psql lampadas -qf dtd.sql
psql lampadas -qf format.sql
psql lampadas -qf language.sql
psql lampadas -qf license.sql
psql lampadas -qf notes.sql
psql lampadas -qf pub_status.sql
psql lampadas -qf review_status.sql
psql lampadas -qf role.sql
psql lampadas -qf stats.sql
psql lampadas -qf stats_cdf.sql
psql lampadas -qf string.sql
psql lampadas -qf string_i18n.sql
psql lampadas -qf subtopic.sql
psql lampadas -qf topic.sql
psql lampadas -qf topic_i18n.sql
psql lampadas -qf username.sql
psql lampadas -qf username_notes.sql
