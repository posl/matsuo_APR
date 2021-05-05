#include <stdio.h>
#include <string.h>
int main(){
    char x[100], y[100];
    int i;
    scanf("%s", x);
    for(i=0; i<strlen(x); i++){
       y[i]=x[strlen(x)-i-1]; 
    }
    y[strlen(x)]='\0';
    strcat(x,y);
    printf("%s",x);
}
