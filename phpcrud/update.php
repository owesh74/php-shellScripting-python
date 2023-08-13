<?php

$servername = "localhost";
$username = "diituser";
$password = "%TGBbgt5";
$dbname = "alpha";

try {
  $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $id = $_REQUEST['id'];
  $sql = "SELECT * FROM employees WHERE id=$id";
  $conn->exec($sql); 

  $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
  $records= $stmt->fetch();



   } catch(PDOException $e) {
     echo "Error: " . $e->getMessage();
   }
$conn = null;
?>
<form action="update_action.php">
<input placeholder name="id" value="<?php echo $records['id']; ?>" type="text" /> <br/>
<input  placeholder name= "name" value="<?php echo $records['name']; ?>" type="text" /> <br/>
<input placeholder name ="contact number" value="<?php echo $records['contact_number']; ?>" type="text" /> <br/>
<input  placeholder name ="addres" value="<?php echo $records['address']; ?>" type="text"/> <br/>
<input  placeholder name ="salary" value="<?php echo $records['salary']; ?>" type="text" /> <br/>
<input  placeholder name ="employee id" value="<?php echo $records['employee_id']; ?>" type="text"/> <br/>
<input   placeholder name ="role" value="<?php echo $records['role']; ?>" type="text"/> <br/>
<input type ="submit"/>
</form>
