#include <iostream>
#include <string>

using namespace std;




int main() {
    // 여기에 코드를 작성해주세요.
    string str ;
    cin >> str ;

    int len = str.length() ;

    char temp ;
    char f = str[0];
    char s = str[1];

    for (int i = 0 ; i < len ; i++) {
        if (str[i]== f) {
            str[i] = s;
            continue;
        }

        if (str[i]== s){
            str[i] = f;
        }

    }

    cout << str ;
    return 0;
}