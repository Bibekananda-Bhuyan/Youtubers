<?php
include('config.php');
session_start();
$currentuseremail=$_SESSION["useremail"];

if (isset($_POST['updatecd'])) {
	# code...
	extract($_POST);
	$sql="UPDATE `users` SET name='$name',email='$email',pass='$pass',phoneno='$phoneno',about='$about',address='$address',website='$website',youtube_ch_link='$youtube_ch_link',insta_id='$insta_id',location='$location',shortdesc='$shortdesc'";
	$conn->query($sql);
    header('Location: ../inprofileedit');

}