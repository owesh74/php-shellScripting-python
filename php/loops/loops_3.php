<?php
//$i = readline("enter a number = ");
for ($i = 1 ; $i <= 100; $i++) {
	sleep(1);

   if($i % 5 == 0 && $i % 3 == 0 ) {
	echo"$i fizzz , buzzz\n";
   }
  
   elseif($i % 3 == 0  ) {
	echo"$i fizzz\n";
   }  
   elseif($i % 5 ==  0) {
  	echo"$i buzzz\n";
   }  
   else {
	echo"$i ----\n";
   }
}
?>
