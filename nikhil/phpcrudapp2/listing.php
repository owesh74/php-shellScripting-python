<?php

$servername = "localhost";
$username = "diituser";
$password = "%TGBbgt5";
$dbname = "alpha";

  $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

  $stmt = $conn->prepare("SELECT * FROM employees ORDER BY salary DESC");
  $stmt->execute();

  $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
  $emps = $stmt->fetchAll();
  
//$conn = null;
?>
<a href = "http://ciacloud.in/owesh/nikhil/phpcrudapp/addemp_form.php?">Add Employee</a>

<table border=1>

<?php
$sum =0;
foreach($emps as $e)
{

	$sum = $sum + $e['salary'];

?>
        <tr>
                <td><?php echo $e['id']; ?></td>
                <td><?php echo $e['name']; ?></td>
                <td><?php echo $e['address']; ?></td>
                <td><?php echo $e['salary']; ?></td>
                <td><?php echo $e['salary']*12/10; ?></td>
		<td><?php echo $e['employee_id']; ?></td>
		<td><?php echo $e['role']; ?></td>
		<td><a onclick="return confirm('Do you really want to delete records of <?php echo $e['name']; ?>');" href="delete.php?id=<?php echo $e['id']?>">delete </a>
		<a href="update.php?id=<?php echo $e['id']?>">update</a>		


</td>
        </tr>
<?php } ?>
<thead>
        <th>id</th>
        <th>Name</th>
        <th>Address</th>
	<th>Salary <?php echo "(total salary = $sum)"?></th>
	<th>Tax 10%</th>
	<th>Employee_id</th>
	<th>Role</th>
	<th>Actions</th>

</thead>
</table>
<br>
<br>

<?php
  $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

  $stmt = $conn->prepare("SELECT id, name, address, salary FROM employees WHERE salary = (SELECT salary FROM employees ORDER BY salary DESC LIMIT 3,1 );");
  $stmt->execute();

  $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
  $emps = $stmt->fetchAll();
?>
<table border=1>

<?php

foreach($emps as $e)
{
?>
        <tr>
                <td><?php echo $e['id']; ?></td>
                <td><?php echo $e['name']; ?></td>
                <td><?php echo $e['address']; ?></td>
                <td><?php echo $e['salary']; ?></td>
             
        </tr>
<?php } ?>
<thead>
        <th>id</th>
        <th>Name</th>
        <th>Address</th>
        <th>Salary </th>
</thead>
</table>

