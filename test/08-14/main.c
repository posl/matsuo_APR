#include <stdio.h>
#include <math.h>

/*f(x)*/
double f(double x,double a,double b,double c)
{
    return a * pow(x,2) + b * x + c;
}

/*f(x)の導関数*/
double g(double x,double a,double b)
{
    return 2 * a * x + b;
}

int main()
{
    //利用する変数
    double x, new_x, eps;
    int number,i;
    double a,b,c;

    //fxの取り込み
    //printf("a : ");
    scanf("%lf",&a);
    //printf("b : ");
    scanf("%lf",&b);
    //printf("c : ");
    scanf("%lf",&c);

    //データの取り込み
    //printf("初期値 : ");
    scanf("%lf",&x);
    //printf("計算精度 : ");
    scanf("%lf",&eps);
    //printf("繰り返し上限回数 : ");
    scanf("%d",&number);
    //printf("繰り返し\tnew x\t\tf(x)\t\tg(x)\n");
    
    /* ニュートン法による解の導出 */
    for(i=0;i<number;i++){
        new_x = x - f(x,a,b,c) / g(x,a,b);
        /* 収束条件で判定し、解を出力 */
        if(fabs(new_x - x) < eps && (g(x,a,b) > 0.0001)){
            printf("%f\n", new_x);
            break;
        }

        //printf("%2d\t\t%f\t%f\t%f\n", i, new_x, f(x,a,b,c), g(x,a,b));

         /* 収束条件、重解の判定をし、重解を出力 */
        if((fabs(new_x - x) < eps) && (g(x,a,b) <= 0.0001)){
            printf("%f(重解)\n", new_x);
            break;
        }
        x = new_x;
    }
    if(i == number) printf("繰り返し上限\n");
}