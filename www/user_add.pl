#! /usr/bin/perl

use Lampadas;
$L = new Lampadas;

$username	= $L->Param('username');
$first_name	= $L->Param('first_name');
$middle_name	= $L->Param('middle_name');
$surname	= $L->Param('surname');
$email		= $L->Param('email');
$admin		= $L->Param('admin');

%newuser = $L->AddUser($username, $first_name, $middle_name, $surname, $email, $admin, '');
$L->Redirect("user_edit.pl?user_id" . $newuser{id});
