#include<stdio.h>
int main() {
    int num;
    printf("enter 1st digit ");
    scanf("%d" , &num);
    
    int num2;
    printf("enter 1st digit ");
    scanf("%d" , &num2);
    
    int num3;
    printf("enter 1st digit ");
    scanf("%d" , &num3);

    int mean = (num + num2 + num3) / 3;
    printf("mean of 3 number is %d" , mean);
}