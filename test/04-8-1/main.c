#include <stdio.h>
#include <math.h>

int main()
{
    int i;
    double ip = 0.0;
    double u[3];
    double v[3];
    
    
    for(i=0; i<3; i++){
        scanf("%lf", &u[i]);
    }
    
        
    for(i=0; i<3; i++){
        scanf("%lf", &v[i]);
    }
    
    for (i=0; i<3; i++){
        ip = ip + u[i]*v[i];
    }
    printf("%f\n", ip);
    
    return 0;
}