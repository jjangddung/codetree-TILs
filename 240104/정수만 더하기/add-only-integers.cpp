#include <iostream>
#include <string>
#include <cctype>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string s ;
    cin  >> s;
    int sum = 0 ;
    int n;


    int k = s.length();

    for (int i = 0 ; i < k ; i++) {
        if (isdigit(s[i]) !=0) {
            // cout << s[i] << endl ;
            n = int(s[i]) - (int)'0';
            sum += n;
            
        }
    }

    cout << sum ;
    return 0;
}