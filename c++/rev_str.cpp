#include <iostream>
//#include <string>

using namespace std;
void revstr(const string);


int main()
{
	string str;
	cout<<"enter a string: "<<endl;
	getline(cin,str);
	revstr(str);
	return 0;
}

void revstr(const string str)
{
	int len = str.length();
	cout<<"length of entered string is "<<len<<endl;
	int k;
	char rev_string[100];
	k = len-1;
	for(int i = 0; i<len; i++)
	{
		rev_string[i] = str[k];
		k--;
	}
	cout<<"reversed string is: "<<rev_string<<"\n";
}
