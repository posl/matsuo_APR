#include <stdio.h>
#define M 10

void mergesort(int a[], int left, int right,int N){
    int mid,i,j,k,tmp[N];
    if (left >= right) return;
    
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