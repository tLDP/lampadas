#!/usr/bin/perl
# 
# Generates a navigation bar suitable for display across the top or bottom of a page.
# 
package Lampadas::Database;

use strict;

use Pg;
use Exporter;
use FileHandle;

my @ISA	= qw(Exporter);
my @EXPORT	= qw(
		new,
		Row,
		Value,
		Exec);

my $conn;
my $debug = 0;
my $foo;

sub _initialize {
	$conn=Pg::connectdb("dbname=lampadas");
}

sub new {
	my $self = {};
	bless $self;
	$self->_initialize();
	return $self;
}

sub Recordset {
	my $self = shift;
	my $sql = shift;
	my $result = $conn->exec("$sql");
	die $conn->errorMessage unless PGRES_TUPLES_OK eq $result->resultStatus;
	return $result;
}

sub Row {
	my $self = shift;
	my $sql = shift;
	my $result = $conn->exec("$sql");
	die $conn->errorMessage unless PGRES_TUPLES_OK eq $result->resultStatus;
	my @row = $result->fetchrow;
	return @row;
}

sub Value {
	my $self = shift;
	my $sql = shift;
	my @row = Row($foo, $sql);
	my $value = $row[0];
	$value =~ s/\s+$//;
	return $value;
}

sub Exec {
	my $self = shift;
	my $sql = shift;
	if ($debug) {
		my $sqllog = new FileHandle;
		open $sqllog, "> /home/david/ldp/cvs/LDP/lampadas/www/sql.log";
		print $sqllog $sql . "\n";
		close $sqllog;
	}
	$conn->exec("$sql");
}
1;
