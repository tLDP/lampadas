#! /usr/bin/perl

use CGI qw(:standard);
use Pg;

$query = new CGI;
$dbmain = "ldp";
@row;

# Read parameters
$doc_id        = param('doc_id');
$title         = param('title');
$title         =~ s/\'/\'\'/;
$filename      = param('filename');
$filename      =~ s/\'/\'\'/;
$class         = param('class');
$format        = param('format');
$dtd           = param('dtd');
$dtd_version   = param('dtd_version');
$version       = param('version');
$version       =~ s/\'/\'\'/;
$last_update   = param('last_update');
$url           = param('url');
$isbn          = param('isbn');
$pub_status    = param('pub_status');
$review_status = param('review_status');
$tickle_date   = param('tickle_date');
$ref_url       = param('ref_url');
$pub_date      = param('pub_date');
$tech_review_status = param('tech_review_status');
$maintained    = param('maintained');
$license       = param('license');
$abstract      = param('abstract');
while ($abstract =~ /\'/) {
	$abstract      =~ s/\'/a1s2d3f4/;
}
while ($abstract =~ /a1s2d3f4/) {
	$abstract      =~ s/a1s2d3f4/\'\'/;
}

$version       =~ s/\'/\'\'/;

$save		= param('save');
$saveandexit	= param('saveandexit');

$conn=Pg::connectdb("dbname=$dbmain");

$username = $query->remote_user();
$result=$conn->exec("SELECT username, admin, maintainer_id FROM username WHERE username='$username'");
@row = $result->fetchrow;
if ($username ne $row[0]) {
	print $query->redirect("../newaccount.html");
	exit;
} else {
	if ($row[1] ne 't') {
		$maintainer_id = $row[2];
		$result=$conn->exec("SELECT count(*) FROM document_maintainer WHERE maintainer_id=$maintainer_id AND doc_id=$doc_id AND active='t'");
		@row = $result->fetchrow;
		unless ($row[0]) {
			print $query->redirect("../wrongpermission.html");
			exit;
		}
	}
}

#This is horribly inefficient, but allows partial saves.
#For our volume, it hardly matters.
$sql = "UPDATE document SET title='$title' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET filename='$filename' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET class='$class' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET format='$format' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET dtd='$dtd' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET dtd_version='$dtd_version' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET version='$version' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET last_update='$last_update' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET url='$url' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET isbn='$isbn' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET pub_status='$pub_status' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET review_status='$review_status' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);

if ( $tickle_date eq '' )
{  $sql = "UPDATE document SET tickle_date=NULL WHERE doc_id=$doc_id"; }
else
{  $sql = "UPDATE document SET tickle_date='$tickle_date' WHERE doc_id=$doc_id"; }
$result=$conn->exec($sql);

$sql = "UPDATE document SET ref_url='$ref_url' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET pub_date='$pub_date' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET tech_review_status='$tech_review_status' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET maintained='$maintained' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET license='$license' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);
$sql = "UPDATE document SET abstract='$abstract' WHERE doc_id=$doc_id";
$result=$conn->exec($sql);

if ($save) {
	print $query->redirect("document_edit.pl?doc_id=$doc_id");
} elsif ($saveandexit) {
	print $query->redirect("document_list.pl");
}


print header;
print start_html;
print "<p>sql: $sql";
print "<p>save: $save";
print "<p>saveandexit: $saveandexit\n";
print end_html;
exit;

