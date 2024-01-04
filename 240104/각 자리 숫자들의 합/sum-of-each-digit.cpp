#include <iostream>
#include <string>
#include <cctype>

using namespace std; 




int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n ;

    string str ;

    str = to_string(n) ;

    int len = str.length();

    int sum = 0 ;

    for (int i = 0 ; i < len ; i ++) {
        sum += (int)(str[i]-'0');

    }

    cout << sum ;

    return 0;
}