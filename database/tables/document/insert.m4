m4_define(insert, [INSERT INTO document(doc_id, lang, title, short_title, version, isbn,
type_code, format_code, dtd_code, dtd_version,
license_code, license_version, copyright_holder,
abstract, short_desc,
pub_status_code, review_status_code, tech_review_status_code,
pub_date, last_update, tickle_date,
maintained, maintainer_wanted, rating,
sk_seriesid, replaced_by_id, pub_time, mirror_time,
first_pub_date)
VALUES ($1, 'I18N_lang_code', '$2', '$3', '$4', '$5',
'$6', string_or_null($7), '$8', '$9',
'$10', '$11', '$12',
'$13',, '$14',
'$15', '$16', '$17',
string_or_null($18), string_or_null($19), string_or_null($20),
'$21', '$22', $23,
'$24', $25, '$26', '$27',
'$28');])m4_dnl

