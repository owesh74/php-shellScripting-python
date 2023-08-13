//wap to read 3 numbers from comand line and find greatest among them
 
args = process.argv
x = parseINT(args[2])
y = parseINT(args[3])
z = parseINT(args[4])


if(x > y && x > z)
	console.log(` ${x} is greater`)
else if( y > z)
	console.log(` ${y} is greater`)
else
	console.log(` ${z} is greater`)

