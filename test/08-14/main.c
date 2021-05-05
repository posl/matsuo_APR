#include <stdio.h>
#include <math.h>

/*f(x)の出力*/
void function()
{
    printf("f(x) = pow(x,2) - 2\n");
}

/*f(x)*/
double f(double x)
{
    return pow(x,2) - 2;
}

/*f(x)の導関数*/
double g(double x)
{
    return 2 * x;
}

int main()
{
    //利用する変数
    double x, new_x, eps;
    int number,i;

    //データの取り込み
    function();
    printf("初期値 : ");
    scanf("%lf",&x);
    printf("計算精度 : ");
    scanf("%lf",&eps);
    printf("繰り返し上限回数 : ");
    scanf("%d",&number);
    printf("繰り返し\tnew x\t\tf(x)\t\tg(x)\n");
    
    /* ニュートン法による解の導出 */
    for(i=0;i<number;i++){
        new_x = x - f(x) / g(x);
        /* 収束条件で判定し、解を出力 */
        if(fabs(new_x - x) < eps && (g(x) > 0.0001)){
            printf("x = %f\n", new_x);
            break;
        }

         printf("%2d\t\t%f\t%f\t%f\n", i, new_x, f(x), g(x));

         /* 収束条件、重解の判定をし、重解を出力 */
        if((fabs(new_x - x) < eps) && (g(x) <= 0.0001)){
            printf("x = %f(重解)\n", new_x);
            break;
        }
        x = new_x;
    }
    if(i == number) printf("繰り返し上限\n");
}