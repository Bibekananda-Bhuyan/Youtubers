<?php
include('config.php');

if(isset($_POST['createuser'])){
extract($_POST);
$name=$fname.$lname;
$tdate=date('y-m-d');
$d2 = new Datetime("now");
$currenttimestap= $d2->format('U');
$ucode=$fname.$currenttimestap;
$sql="INSERT INTO `users` (name,email,pass,phoneno,atype,dateofjoin,verificationuid) VALUES('$name','$useremail','$userpass','$userpgoneno','$inlineMaterialRadiosExample','$tdate','$ucode')";
if ($conn->query($sql) === TRUE) {
header('Location: ../signupthanks');
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

}