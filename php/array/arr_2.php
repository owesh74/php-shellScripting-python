<?php
$emps =[
	["name" => "tushar" , "salary" => 20000],
	["name" => "nikhil" , "salary" => 53000],
	["name" => "shrikant" , "salary" => 67000]
];

//echo "<pre>";
//print_r($emps);
//echo "<pre/>";

?>

<table border=1>
<thead>
	<th>name</th>
	<th>salary</th>
	<th>tax</th>
<thead>
	
<?php foreach($emps as $e){ ?>
	<tr>
		<td><?php echo $e['salary']; ?></td>
		<td><?php echo $e['name']; ?></td>
		<td><?php echo $e['salary ']*12; ?></td>
	</tr>
<?php
}


?>
</table>

