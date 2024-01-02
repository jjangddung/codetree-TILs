#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string str;

    cin >> str ;

    char temp = str[1];

    int len = str.length();

    for (int i = 0 ; i < len ; i ++) {
        if (str[i]== temp) {
            str[i]= str[0];
        }

        cout << str[i];
    }
    return 0;
}