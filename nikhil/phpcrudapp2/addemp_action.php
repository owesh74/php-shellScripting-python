<?php
$servername = "localhost";
$username = "diituser";
$password = "%TGBbgt5";
$dbname = "alpha";
$name = $_REQUEST['name'];
$cnum = $_REQUEST['contact_number'];
$address = $_REQUEST['address'];
$sal = $_REQUEST['salary'];
$empid = $_REQUEST['employee_id'];
$role = $_REQUEST['role'];
try {
  $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $sql = "INSERT INTO employees(id,name,contact_number,address,salary,employee_id,role,created_at,updated_at) VALUES (NULL,'$name',$cnum,'$address',$sal,$empid,'$role',NOW(),NOW())";
  $stmt = $conn->prepare("$sql");
  $stmt->execute();

  $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
  $emps=$stmt->fetch();
} catch(PDOException $e) {
  echo "Error: " . $e->getMessage();
}
$conn = null;
header("Location:http://ciacloud.in/owesh/nikhil/phpcrudapp/listing.php");
?>

