#include <stdio.h>

int main(void)
{
    int i;
    float j;
    unsigned int u;
    float f;
    
    i = 077;
    j = 3.14;
    u = -255;
    f = 10;
    
    printf("i = %o\n", i);
    printf("j = %1.2f\n", j);
    printf("u = %d\n", u);
    printf("f = %2.1f\n", f);
}
