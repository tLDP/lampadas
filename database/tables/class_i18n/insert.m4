m4_changequote([, ])m4_dnl
m4_define(insert,m4_dnl
[INSERT INTO class_i18n(class_id, lang, class_name, class_description)
VALUES ('$1', 'I18N_lang_code', '$2', '$3');])m4_dnl
