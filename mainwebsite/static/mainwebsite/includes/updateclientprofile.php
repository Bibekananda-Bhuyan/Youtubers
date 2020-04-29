<?php
include('config.php');
session_start();
$currentuseremail=$_SESSION["useremail"];

if (isset($_POST['updatecd'])) {
	# code...
	extract($_POST);
	$sql="UPDATE `users` SET name='$name',email='$email',pass='$pass',phoneno='$phoneno',about='$about',address='$address',website='$website' where email='$currentuseremail'";
	$conn->query($sql);
    header('Location: ../clientprofile');

}