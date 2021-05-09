#include<stdio.h>
#include<math.h>

/* f(x) */
void bubble(int a[],int left,int right){
    int i, j, tmp;
    for(i = left; i < right - 1; i++){
        for(j = i + 1; j < right; j++){
            /* もしもa[j]がa[i]より小さいならばa[i]とa[j]を入れ替える */
            if(a[j] < a[i]){
                tmp = a[j];
                a[j] = a[i];
                a[i] = tmp;
            }
        }
    }
}

int main()
{
    int N, i;

    //要素数
    scanf("%d", &N);
    int a[N];

    //入力データを配列a[N]に格納
    for(i=0;i<N;i++){
        scanf("%d",&a[i]);
    }

    bubble(a,0,N);
    //ソート結果を出力
    for(i=0;i<N;i++){
        printf("%d\n",a[i]);
    }
}