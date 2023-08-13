#include<stdio.h>
void ind();
void frn();
int main (){
char user;
printf("enter your country 'i' for india 'f' for french : ");
scanf("%c" , &user);

if(user == 'i')
     ind();
else if(user == 'f')
     frn();
else
printf("invalid input");

    return 0;
}
 void ind() {
    printf("namaste");
 }
 void frn() {
    printf("bonjour");
 }