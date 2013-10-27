#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int l;
bool loop(int i,string &s1,string &s2){
    for (int j=0; j<l; ++j){
        if (s1[(l-1-i+j)%l]==s2[j]){
        }else{
            return false;
        }
    }
    return true;
}

int main()
{
    string s1;
    string s2;
    while (! (cin>>s1).eof()){
        /*if (feof(stdin)){
            break;
        }*/
        cin >> s2;
        //cout << s1.size();
        l = s1.size();
        if (s2.size()!=l){
            cout <<"-1\n";
            continue;
        }
        if (s1==s2){
            cout << "0\n";
            continue;
        }
        bool got=false;
        for (int i=0; i<l;++i){
            // try matching i+1th from last of s1
            if (loop(i,s1,s2)){
                cout << i+1 <<"\n";
                got=true;
                break;
            }
        }
        if (not got){
            cout << "-1\n";
        }
    }
    return 0;
}
