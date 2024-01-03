#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string s ;
    string p ;
    cin >> s>> p ;

    int k = s.length();
    int l = p.length();

    for (int i = 0 ; i < l ; i ++) {
        if (p[i]== 'L') {
            s = s.substr(1,k-1) + s.substr(0,1);
        }

        else {
            s = s.substr(k-1,1) + s.substr(0,k-1);
        }
    }

    cout << s;
    return 0;
}