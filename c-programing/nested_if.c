#include<stdio.h>

int main() {
int num;
printf("enter ANY number = ");
scanf("%d" , &num);
if(num >= 0){
    printf("number is positive");
    if(num % 2 == 0){
    printf("\nnumber is even");
    }
    else{
    printf("\nnumber is odd");
    }

}
else{
    printf("number is negetive");
}