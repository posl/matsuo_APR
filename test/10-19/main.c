#include <stdio.h>
#include <math.h>
#define M 4

int main(){

    //変数宣言
    double a[M][M];
    double b[M];
    double c[M];
    double l[M][M];
    double u[M][M];
    double x[M];
    int i, j, k;
    double d;

    //入力データの受け取り
    for(i=0;i<M;i++){
        for(j=0;j<M;j++) scanf("%lf",&a[i][j]);
    }
    for(i=0;i<M;i++) scanf("%lf",&b[i]);

    //L行列，U行列の初期化
    for(i=0;i<M;i++){
        for(j=0;j<M;j++){
            u[i][j]=0;
            if(i==j) l[i][j]=1;
            else l[i][j]=0;
        }
    }

    //入力行列の出力(ピボッティングでa行列を操作するため事前に出力)
    printf("入力行列\n");
    for(i=0;i<M;i++){
        for(j=0;j<M;j++) printf("%10.5lf",a[i][j]);
        printf("%10.5lf\n",b[i]);
    }

    for(i=0;i<M;i++){
        //行交換
        for(j=i; j<M; j++){
            if(fabs(a[i][i]) < fabs(a[j][i])){
                for (k = 0; k < M; ++k) {
                    d = a[i][k];
                    a[i][k] = a[j][k];
                    a[j][k] = d;
                }
                d = b[i];
                b[i] = b[j];
                b[j] = d;
                for (k=0; k<i; k++){
                    d = l[i][k];
                    l[i][k] = l[j][k];
                    l[j][k] = d;
                }
            }
        }

        //U行列の生成
        for(j=i;j<M;j++){
            u[i][j]=a[i][j];
        }
        //L行列の生成
        for(j=i+1;j<M;j++){
            l[j][i] = a[j][i] / u[i][i];
        }

        //新たなaの導出
        for(j=i+1;j<M;j++){
            for(k=i+1;k<M;k++) a[j][k]=a[j][k]-l[j][i]*u[i][k];
        }
    }

    //c行列の生成
    for(i=0;i<M;i++){
        c[i] = b[i];
        for(j=0;j<i;j++) c[i] -= l[i][j]*c[j];
    }

    //x行列の生成
    for(i=M-1;i>=0;i--){
        x[i] = c[i];
        for(j=M-1;j>i;j--) x[i] -= u[i][j]*x[j];
        x[i] /= u[i][i];
    }

    //結果の出力
        //L行列
        printf("\nL行列\n");
        for(i=0;i<M;i++){
            for(j=0;j<M;j++) printf("%10.5lf",l[i][j]);
            printf("\n");
        }
        //U行列
        printf("\nU行列\n");
        for(i=0;i<M;i++){
            for(j=0;j<M;j++) printf("%10.5lf",u[i][j]);
            printf("\n");
        }
        //解の出力
        for(i=0;i<M;i++) printf("x%d = %10.5lf\n",i,x[i]);
}