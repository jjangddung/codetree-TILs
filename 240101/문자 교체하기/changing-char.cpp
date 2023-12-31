#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string first ;
    string second ;
    cin >> first >> second ;

    int f_len = first.length();
    int s_len = second.length();

    for (int i = 0 ; i  <= s_len-1 ; i++) {
        if (i <=1) {
            second[i] = first[i];
        }
        cout << second[i] ;
    }
    return 0;
}