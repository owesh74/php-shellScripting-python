#include<stdio.h>

int main() {
    int b;
    printf("give a number : ");
    scanf("%d" , &b);
    int i =1;
    do {
        printf("%d\n" , i);
        i++;
    } while(i <= b);

}