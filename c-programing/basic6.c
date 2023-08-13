#include<stdio.h>
int main(){
    int num;
    printf("give a 4 digit number = ");
    scanf("%d" ,&num);
    int a = (num / 1000) % 10;
    int b = (num / 100) % 10;
    int c = (num % 100) / 10;
    int d = num % 10;
    int sum = a + b + c + d;
    
    
    printf("addition of %d + %d + %d + %d = %d " , a ,  b , c , d , sum);
    return 0;

}