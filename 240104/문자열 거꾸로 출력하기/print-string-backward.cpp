#include <iostream>
#include <string>


using namespace std;


int main() {
    // 여기에 코드를 작성해주세요.
    string str;

    while (true) {
        cin >> str;

        if (str ==  "END") {
            break;
        }

        int k = str.length() ;

        for (int i = k-1 ; i >= 0 ; i--) {
            cout << str[i];
        }
        cout << endl ;
    }
    return 0;
}