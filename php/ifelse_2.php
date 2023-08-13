<?php
$num1 = readline("enter 1st number = ");
$num2 = readline("enter 2ed number = ");
$num3 = readline("enter 3rd number = ");

if( $num1 > $num2 && $num1 > $num3  )  {
	echo" $num1 is greater than $num2 & $num3\n";
} 
if( $num2 > $num1 && $num2 > $num3  )  {
	echo" $num2 is greater than $num1 & $num3\n";
}
else {
	echo" $num3 is greater than $num1 & $num2\n";
}
?>
