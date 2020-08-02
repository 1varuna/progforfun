#include <iostream>
using namespace std;

int main()
{
	int n, revNum=0, rem;

	cout<<"enter an integer: ";
	cin>>n;

	while(n!=0)
	{
		rem = n%10;
		revNum = revNum*10+rem;
		n = n/10;
	}

	cout<<"\t reversed number is = "<<revNum<<"\n";

	return 0;
}
