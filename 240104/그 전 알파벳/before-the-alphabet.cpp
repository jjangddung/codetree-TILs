#include <iostream>

using namespace std ;

int main() {
    // 여기에 코드를 작성해주세요.
    char a ;
    cin >> a;


    int k  = (int)a;

    if (a == 'a') {
        cout << 'z';
    }

    else {
        cout << (char)(k-1);
    }
    return 0;
}