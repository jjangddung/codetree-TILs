#include <iostream>
#include <string>
#include <cctype>

using namespace std ;




int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n ;
    string str;

    int sum = 0 ;
    string sum_str ;

    for (int i = 0 ; i < n ; i ++) {
        cin >> str;

        sum += stoi(str);

        
    }

    sum_str = to_string(sum);

    int len = sum_str.length() ;
    cout << sum_str.substr(1,len-1) + sum_str.substr(0,1) ;

    return 0;
}