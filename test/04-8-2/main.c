#include <stdio.h>
#include <math.h>

int main()
{
    int i, j, k;
    float answer;
    float a[3][3], b[3][3], c[3][3];
    
    for(i=0; i<3; i++){
        for(j=0; j<3; j++){
                scanf("%f", &a[i][j]);
        }
    }
    
    for(i=0; i<3; ++i){
        for(j=0; j<3; ++j){
                scanf("%f", &b[i][j]);
        }
    }
    
    //行列の積
    for(i=0; i<3; ++i){
        for(j=0; j<3; ++j){
            c[i][j] = a[i][j]*b[i][j];
            
            for(i=0; i<3; ++i){
                for(j=0; j<3; ++j){
                    answer = 0;
                    for (k=0; k<3; ++k){
                        answer = answer + a[i][k]*b[k][j];
                        c[i][j] = answer;
                    }
                }
            }
        }
    }
    
    for(i=0; i<3; ++i){
        for(j=0; j<3; ++j){
            printf("%f\n",c[i][j]);
        }
    }
    
    return 0;
}

