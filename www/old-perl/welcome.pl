#!/usr/bin/perl
#
use Lampadas;
$L = new Lampadas;

$project = $L->Config('project');
$L->StartPage("Welcome");
print $L->String(1);
$L->EndPage();

