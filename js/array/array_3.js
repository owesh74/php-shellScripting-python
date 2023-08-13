nums = [ 1 , 2 , 2 , 4 , 3]
sum = 2
is_found = false

for(i= 0; i < nums.length; i++)  {
	if(sum == nums[i]) {
		is_found = true
		break
}

}

if(is_found == true)
	console.log(`${sum} found at position ${i+1}`)
else
	console.log(` ${sum} not found`)



