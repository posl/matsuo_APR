#include <stdio.h>

int main()
{
    int i, n;
    scanf("%d" ,&n);

    float a[n];
    float sum, sum2, ave, dis;
    
    sum = 0.0;
    sum2 = 0,0;
    for (i = 0; i < n; i++)
    {
        scanf("%f" , &a[i]);
        sum += a[i];
        sum2 += a[i]*a[i];
    }
    ave = sum / n;
    dis = (sum2 / n) - (ave * ave);
    printf("%.3f\n" , ave);
    printf("%.3f\n" , dis);
    
    return 0;
}