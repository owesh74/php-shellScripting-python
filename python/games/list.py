"""
fruits = ["apple", "mango", "orange"];

print(fruits[1]);


print(len(fruits))


for x in range(0, len(fruits)):
    print(fruits[x]);
 """

matrix = [
            [1, 2, 3], 
            [4, 5, 6],
            [7, 8, 9]
        ];



for i in range(0, len(matrix)):
    for j in range(0, 3):
        print(matrix[i][j], end="\t");

    print("\n");



interstaller = [
                [
                    [
                        [[1, 2, [3, 4]]]
                        ]
                    ]
            ];

print(interstaller[0][0][0][0][2][1]);
#print(interstaller[0][0][0][0][0][2][1]);
