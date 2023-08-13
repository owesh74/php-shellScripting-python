#include<stdio.h>
 int main(){
    int fact =1;
    int n;

    printf("give a number : ");
    scanf("%d" , &n);
  for(int i=1; i <= n; i++){
    fact = fact * i ;
  }
   printf("%d\n" ,  fact);  
   
 }