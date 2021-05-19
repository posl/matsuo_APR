#include <stdio.h>

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

void mergesort(int a[], int left, int right,int N){
    int mid,i,j,k,tmp[N];
    if (left >= right) return;
    if (right-left<32){
        bubble(a,left,right+1);//bubbleのrightは配列の終端より一つ右を指すので，ここで1を加えて補正
    }
    else{
        //要素を分解
        mid = (left+right)/2;
        mergesort(a,left,mid,N);
        mergesort(a,mid+1,right,N);

        //要素を統合
        for(i=left;i<=mid;i++) tmp[i]=a[i];
        for(j=mid+1;j<=right;j++) tmp[right-(j-(mid+1))]=a[j];
        i=left;
        j=right;
        for(k=left;k<=right;k++){
            if(tmp[i]<tmp[j]) a[k]=tmp[i++];
            else a[k] = tmp[j--];
        }
    }
}

int main(){
    int N,i;
    scanf("%d",&N);
    int a[N];

    //入力の取り込み
    for(i=0;i<N;i++)scanf("%d",&a[i]);

    mergesort(a,0,N-1,N);

    //出力の取り込み
    for(i=0;i<N;i++) printf("%d\n",a[i]);
}