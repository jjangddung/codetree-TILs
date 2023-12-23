#include <iostream>

using namespace std;



int main() {
    int s , a ;
    cin >> s>> a;

    if (s== 0) {
        cout << (a<19 ? "BOY":"MAN") ;
    }

    else {
        cout << (a<19 ? "GIRL":"WOMAN") ;
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}