#include<stdio.h>
#include<string.h>
void main()
{
    int i, j, k;
    char str[100];
    char rev[100];
    printf("Enter a string:\t");
    scanf("%s", str);
    
    int len;
    len = strlen(str);
    
    k = len-1;
    
    printf("Length of the entered string is : %d\n",len);
    
    for(j = 0; j <= len-1; j++)
    {
        rev[j] = str[k];
        k--;
    }
    printf("The reverse string is %s\n", rev);
}
