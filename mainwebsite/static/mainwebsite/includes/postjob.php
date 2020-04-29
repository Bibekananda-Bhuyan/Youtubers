<?php
include('config.php');
session_start();
$currentuseremail=$_SESSION["useremail"];
if(isset($_POST['MAKEJPOST'])){
extract($_POST);
$tdate=date('y-m-d');

$sql="INSERT INTO `postedjob` (useremailid,contactname,contactno,post_category,project_budget,work_description,influencer_platform,influencer_id,posted_date,projecttitel) VALUES('$currentuseremail','$cname','$cphone','$category','$projectbudget','$workdescription','$platfrom','$influencer_id','$tdate','$projecttitel')";

	if ($conn->query($sql) === TRUE) {

		header('Location: ../postedthanks');
	} 
	else {
	    echo "Error: " . $sql . "<br>" . $conn->error;
	}

}