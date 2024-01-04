#include <iostream>
#include <string>
#include <cctype>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    int a,b;
    cin >> a>> b;

    a  += b;

    string s;


    s = to_string(a);

    int len = s.length();
    int cnt = 0 ;

    for (int i = 0 ; i < len ; i++) {
        if (s[i]== '1') {
            cnt += 1;

        }
    }

    cout << cnt ;
    return 0;
}