#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string s ;
    cin >> s;

    string f = s ;

    int k = s.length();

    cout << s;
    cout << endl ;



    while (true) {
        s = s.substr(k-1,1) + s.substr(0,k-1);
        cout << s;
        cout << endl ;

        if (s == f) {
            break;
        }

        

    }
    return 0;
}