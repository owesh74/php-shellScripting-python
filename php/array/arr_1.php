<?php

$arr = [1,2,3,4,5,6];

?>
<h1>

<?php

	echo $arr[3]; 

?>

</h1>

<h2>

<?php echo "cube of $arr[3] is ". ($arr[3] * $arr[3] * $arr[3]); ?>

</h2>
<ul>
<?php
foreach($arr as $x){
?>


<li>

<?php


	echo "square of $x is ".($x * $x); 

?>
</li>


<?php
}
?>
</ul>
