#include<stdio.h>
int main(){
int b;
do{
    printf("give a number :");
    scanf("%d" , &b);
    printf("%d \n" , b);

    if (b % 7 == 0 ) {
        break;
        }
}

while(1);
printf("end");
}