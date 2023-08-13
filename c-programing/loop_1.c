#include<stdio.h>

int main() {
    int b;
    printf("give a number : ");
    scanf("%d" , &b);
    int sum = 0;
    for(int i=1 , j=b ; i <= b && j >= 1 ; i++ , j-- ){
        sum = sum + i;
      printf("%d\n" , j);      
    }
  printf("sum of number %d\n" , sum);

  //for(int i=b ; i >= 1 ; i-- ){
  //      printf("%d\n" , i);
   //S }
  

}
