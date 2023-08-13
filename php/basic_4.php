<?php
$num = readline("enter 4 digit number = ");

$a1 =  intdiv($num ,1000);
$a2 =  ($num / 100) % 10;
$a3 =  ($num / 10)  % 10;
$a4 =   $num % 10;

echo "sum of $a1 + $a2 + $a3 + $a4 is".($a1 + $a2 + $a3 + $a4)."\n";


?>
