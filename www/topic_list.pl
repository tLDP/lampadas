#!/usr/bin/perl
#
use Lampadas;
use Lampadas::Database;

$L = new Lampadas;
$DB = new Lampadas::Database;

$L->StartPage('Topic Listing');

print $L->TopicsTable();

$sql = "SELECT topic.topic_num, topic.topic_name, subtopic.subtopic_num, subtopic.subtopic_name, document.doc_id, document.title, topic_description, subtopic_description FROM topic, subtopic, document_topic, document ";
$sql .= "WHERE topic.topic_num = subtopic.topic_num and topic.topic_num = document_topic.topic_num and subtopic.subtopic_num = document_topic.subtopic_num and document_topic.doc_id = document.doc_id AND document.pub_status='N' ";
$sql .= "ORDER BY topic_num, subtopic_num, title";
$recordset=$DB->Recordset($sql);

$last_topic_num = 0;
$last_subtopic_num = 0;

while (@row = $recordset->fetchrow) {
	$topic_num            = $row[0];
	$topic_name           = $row[1];
	$subtopic_num         = $row[2];
	$subtopic_name        = $row[3];
	$doc_id               = $row[4];
	$title                = $row[5];
	$topic_description    = $row[6];
	$subtopic_description = $row[7];

	if ($topic_num != $last_topic_num) {
		print "<p><hr>" if ($last_topic_num);
		print "<h1>$topic_num $topic_name</h1>\n";
		print "<blockquote>$topic_description</blockquote>\n";
	}
	if ($subtopic_num != $last_subtopic_num) {
		print "<h2>$topic_num.$subtopic_num $subtopic_name</h2>\n";
		print "<blockquote>$subtopic_description</blockquote>\n";
	}
	print "<a href='document_edit.pl?doc_id=$doc_id'>$title</a>\n";
	print "<br>\n";

	$last_topic_num = $topic_num;
	$last_subtopic_num = $subtopic_num;
}

$L->EndPage();

