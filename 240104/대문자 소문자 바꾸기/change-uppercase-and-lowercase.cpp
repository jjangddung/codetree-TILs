#include <iostream>
#include <string>
#include <cctype>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string s;

    cin >> s;

    int len = s.length() ;

    for (int i = 0 ; i < len ; i ++) {
        if (s[i] >= 'A' and s[i] <= 'Z') {
            cout << (char) tolower(s[i]);
        }
        else {
            cout << (char) toupper(s[i]);
        }
    }
    return 0;
}