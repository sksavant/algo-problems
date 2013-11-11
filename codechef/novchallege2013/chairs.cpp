#include<iostream>
#include<cmath>

using namespace std;

int main(){
	int t,n;
	cin >> t;
	for (int i=0;i<t;++i){
		cin >> n;
		cout << (((long long unsigned int)pow(2,n))-1)%1000000007 << "\n";
	}
	return 0;
}
