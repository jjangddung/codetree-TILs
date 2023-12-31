#include <iostream>
#include <string>

using namespace std;


int main() {
    // 여기에 코드를 작성해주세요.
    string str ;
    cin >> str ;
    
    int len = str.length();

    for (int i =0 ; i < len  ; i ++) {
        if (i == 1 or i == len -2) {
            str[i] = 'a';
        }
    }
    cout <<  str ;
    return 0;
}