#include <iostream>
#include <string>
#include <cctype>



using namespace std;


int main() {
    // 여기에 코드를 작성해주세요.

    string s ;
    cin >> s;

    int k = s.length();

    for (int i = 0 ; i < k ; i ++) {
        if (isalpha(s[i]) != 0) {
            //cout << s[i] ;
            //cout<< endl ;
            cout << (char) toupper(s[i]);
        }
    }
    return 0;
}