<?php
include('config.php');
session_start();
$currentuseremail=$_SESSION["useremail"];

 
	# code...
	extract($_GET);
	$sql="UPDATE `postedjob` SET canceledbyclient='1',project_status='Canceled' where id='$jid'";
	$conn->query($sql);
    header('Location: ../clientpostedjob');

 