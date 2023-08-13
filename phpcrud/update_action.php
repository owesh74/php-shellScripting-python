<?php

$servername = "localhost";
$username = "diituser";
$password = "%TGBbgt5";
$dbname = "alpha";

try {
  $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $id = $_REQUEST['id'];
  $sql = "select * FROM employees WHERE id=$id";
  $conn->exec($sql);   
   } catch(PDOException $e) {
     echo "Error: " . $e->getMessage();
   }
$conn = null;
header("location: listing.php");
