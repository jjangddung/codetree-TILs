#include <iostream>
#include  <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string s, p ;
    cin >> s >> p ;

    int len = s.length() ;

    bool thing =  false ;

    int k = 0 ;


    for (int i = 0 ; i < len ; i ++) {
        s  = s.substr(len-1,1) + s.substr(0,len-1);
        k += 1;

        if (s== p) {
            cout  << k ;
            thing = true ;
            break;
        }

    }

    if (thing == false) {
        cout << -1;
    }
    return 0;
}