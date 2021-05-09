#include<stdio.h>
#include<math.h>

/* f(x) */
double f(double x)
{
    return exp(-x*x);
}

int main()
{
    double a, b, x, h, sum = 0.0;
    int n, i;

    //積分区間
    scanf("%lf %lf", &a, &b);
    //分割数
    scanf("%d", &n);

    // 台形の面積の計算
    h = (b-a)/n;
    for (i=0; i<n; i++) {	
        x = a + (double)i*h;
        sum += (h/2)*(f(x) + f(x+h));
    }

    printf("%lf\n",sum);

}