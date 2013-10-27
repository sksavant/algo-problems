#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <string>
using namespace std;
vector<int> primes;
void printListofPrimes(){
    return;
}

bool isPrime(int n){
    if (n==1){
        return 0;
    }
    /*
    if (n%2==0){
        return false;

    }*/
    for(int i=0;i<primes.size();++i){
        if (n==primes[i]){
            return 1;
        }
    }
    int i=0;
    int sq = sqrt(n);
    while (true){
        if (i>sq){
            primes.push_back(n);
            return true;
        }
        if ((n%i)==0){
            return false;
        }
        i++;
    }
}

int main()
{
    std::cout << isPrime(3) << std::endl;
    return 0;
    int n;
    while(! (cin>>n).eof()){
        cout << n << endl;
        int p=3;
        while (true){
            cout << isPrime(p) << "S \n";
            if (isPrime(p)==1){
                cout << "OK";
                cout << p << " " << n-p << "\n";
                break;
            }
            p=p+2;
        }
    }
    return 0;
}
