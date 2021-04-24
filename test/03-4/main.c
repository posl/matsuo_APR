#include <stdio.h>
float convC2F(float C)
{
    float F;
    F=(1.8*C)+32.0;
    return F;
}
int main()
{
    float C,F;
    scanf("%f",&C);
    F=convC2F(C);
    printf("%f\n",F);
    return 0;
}