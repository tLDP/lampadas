DELETE FROM string_i18n;
DELETE FROM string;

INSERT INTO string(string_code) VALUES ('test');
INSERT INTO string(string_code) VALUES ('project');
INSERT INTO string(string_code) VALUES ('projectshort');
INSERT INTO string(string_code) VALUES ('mmtitle');
INSERT INTO string(string_code) VALUES ('home');
INSERT INTO string(string_code) VALUES ('doctable');
INSERT INTO string(string_code) VALUES ('docdetails');

INSERT INTO string_i18n(string_code, lang, string) VALUES ('test',		'EN', 'Test Text');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('test',		'FR', 'Le Test Text');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('footer',		'EN', '<h1><center>Lampadas Footer</center></h1>');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('footer',		'FR', '<h1><center>Le Lampadas Footer</center></h1>');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('project',		'EN', 'The Linux Documentation Project');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('project',		'FR', 'Le Linux Documentation Project');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('projectshort',	'EN', 'The LDP');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('projectshort',	'FR', 'Le LDP');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('mmtitle',		'EN', 'Main Menu');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('mmtitle',		'FR', 'Le Main Menu');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('home',		'EN', 'Home');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('home',		'FR', 'Le Home');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('doctable',		'EN', 'DocTable');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('doctable',		'FR', 'Le DocTable');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('docdetails',	'EN', 'Document Details');
INSERT INTO string_i18n(string_code, lang, string) VALUES ('docdetails',	'FR', 'Le Document Details');
