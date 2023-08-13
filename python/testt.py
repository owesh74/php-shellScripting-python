nums= [1,2,55,66,77,8,]
search= 3
flag == True
for i in range(0 , len(nums)):
    if(search == nums[i]):
        print(f" found at position {i +1}")
        flag == False  
        break;
if(flag == True):
    print(" 404 not found")



