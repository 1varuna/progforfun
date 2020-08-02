#include <stdio.h>
#include <stdlib.h>

int fib(int n)
{
	if(n<=1)
	{
		return 1;
		printf("1");
	}
	else {
		int n = (fib(n-1)+fib(n-2));
		printf("%d",n);
		return n;
	}
}

int main()
{
	int num;
	printf("Enter a Range \n");
	scanf("%d",&num);
	int fibo = fib(num);
	printf("\t Sum of Fibonacci series for first %d numbers is %d \n",num,fibo);
	return 0;
}
