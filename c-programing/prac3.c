// wap to take input from user and chek wheater the number +ve -ve or zero;
#include<stdio.h>

int main() {

    int a;
    printf("give a number = ");
    scanf("%d" , &a);

    if(a > 0) {
    printf("%d is +ve" , a);
    }
    if(a < 0)
    printf("%d is -ve" , a);
    if(a == 0)
    printf("number is zero");
}

