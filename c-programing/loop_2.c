#include<stdio.h>
int main(){
int b;
printf("give a number : ");
scanf("%d" , &b);
 
    for(int i=1  ; i <= 10 ; i++){
        //int sn = b * i;
        printf("%d * %d = %d\n" , b , i , b * i );
    }
}