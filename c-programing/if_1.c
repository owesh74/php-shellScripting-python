#include<stdio.h>

int main() {
int age;
printf("enter your age = ");
scanf("%d" , &age);
if(age >= 18 && age <= 29 ) {
    printf("adult\n");
    printf("eligible for marrage\n");
    
}
else if(age >= 30) {
    printf("kya kar raha hai abhi tak");
}
else{
    printf("not adult");
}
printf("\nthank you ");
}