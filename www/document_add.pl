#! /usr/bin/perl

use Lampadas;
use Lampadas::Database;

$L = new Lampadas;

unless ($L->Admin()) {
	print $query->redirect("wrongpermission.pl");
	exit;
}
$title      = $L->Param('title');
$class      = $L->Param('class');
$format     = $L->Param('format');
$dtd        = $L->Param('dtd');
$pub_status = $L->Param('pub_status');

$doc_id = $L->AddDoc($title, undef, $class, $format, $dtd, undef, undef, undef, undef, undef, $pub_status, 'U', undef, undef, undef,'U','t');

$L->Redirect("document_edit.pl?doc_id=$doc_id");

