#include<stdio.h>
int main(){
int b;
printf("give A number : ");
scanf("%d" , &b);
    
for(int i=10 ; i >= 1 ; i--){
printf(" %d * %d = %d \n" , b , i , b * i );
    }
    
}
