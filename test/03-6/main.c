#include <stdio.h>
#include <math.h>

int main()
{
    float a, b, c, d;
    float x1, x2, e1, e2, i;
    scanf("%f %f %f", &a, &b, &c);  // a,b,cに値を代入
    d = (b * b) - (4 * a * c);  // 判別式
    e1 = sqrt(d);  // d>0の時の平方根
    e2 = sqrt(-d);  //  d<0の時の平方根
    if(d < 0){
        x1 = (float)(-b) / (float)(2 * a);  // 実数部
        i = e2 / (2 * a);  // 虚数部
        printf("%f+%fi\n", x1, i);
        printf("%f-%fi\n", x1, i);
    }
    else if(d == 0){
        x1 = (float)(-b + e1) / (float)(2 * a);  // 重解
        printf("%f\n", x1);
    }
    else{
        x1 = (float)(-b + e1) / (float)(2 * a);
        x2 = (float)(-b - e1) / (float)(2 * a);
        printf("%f\n", x1);
        printf("%f\n", x2);
    }
}