#include <stdio.h>
#include <stdlib.h>

int fact(int n)
{
	if(n==1)
		return 1;
	else return n*fact(n-1);
}

int main()
{
	int num;
	printf("Enter a Number \n");
	scanf("%d",&num);
	int factorial = fact(num);
	printf("\t Factorial of %d is %d \n",num,factorial);
	return 0;
}
