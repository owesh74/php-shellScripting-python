#include<stdio.h>

int main() {
    float pi = 3.14;
    int radius;
    printf("give radius : ");
    scanf("%d " , &radius);

    float area = pi * (radius * radius);
    printf("area of circle %f " , area);

    
}