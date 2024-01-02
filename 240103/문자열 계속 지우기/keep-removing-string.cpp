#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.

    string s,l ;
    cin >> s >> l ;

    int k = s.length();
    int t = l.length();
    int i = 0 ;

    while (i < k -t+1) {
        if (s.substr(i,t)== l) {
            s.erase(i,t);
            i = 0 ;
            k = s.length();
        }

        else {
            i++;
        }
    }

    cout << s ;

    return 0;
}