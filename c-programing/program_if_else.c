#include<stdio.h>

int main() {
    int maths;
    printf("enter marks in maths between (0-100) : ");
    scanf("%d" , &maths);
    
    int chem;
    printf("enter marks in chemistry between (0-100) : ");
    scanf("%d" , &chem);
    
    int phy;
    printf("enter marks in physics between (0-100) : ");
    scanf("%d" , &phy);
    
    int eng;
    printf("enter marks in english between (0-100) : ");
    scanf("%d" , &eng);
    
    int bio;
    printf("enter marks in biology between (0-100)  : ");
    scanf("%d" , &bio);
    
    int sum = maths + chem + bio + phy + eng; 
    int per =  sum/5;


    if(maths > 0 && maths <100 && chem > 0 && chem < 100 && phy > 0 && phy < 100 && eng > 0 && eng < 100 && bio > 0 && bio < 100 )

        if(maths >= 35 && chem >= 35 && phy >=35 && eng >= 35 && bio >= 35){
            printf("student is PASS\n");
            printf("student percentage %d \n" , per);
            printf("student marks %d \n" , sum);
                if(per >= 75)
                    printf("Student passed with 1st class Distinction");
                else if(per > 60 && per < 75)
                    printf("student passed with 1st class");
                else if(per > 50 && per <60)
                    printf("student passed with 2ed class");
                else{
                    printf("student passed with 3rd class");
                }
        }
        else{
            printf("student id is FAIL\n");
            printf("student percentage %d \n" , per);
            printf("student marks %d \n" , sum);
        }


     else{
        printf("enter valid marks");
     }   
}



