<?php
include('config.php');
session_start();

if (isset($_POST['gologin'])) {
	# code...
	extract($_POST);

	 $sql="SELECT * FROM `users` WHERE email='$email' AND pass='$password' AND isverifed='1' LIMIT 1" ;
	 $result=$conn->query($sql);
	echo $isfounduser=mysqli_num_rows($result);

	if ($isfounduser>0) {
		# code...

		if ($result = $conn -> query($sql)) {
		  while ($row = $result -> fetch_assoc()) {
		  	$atype=$row['atype'];
		  }
		}

		$_SESSION["useremail"] = $email;
		$_SESSION["currentuser_role"] = $atype;
		
		header('Location: ../index');

	}
	else{
		header('Location: ../loginerror');

	}

}