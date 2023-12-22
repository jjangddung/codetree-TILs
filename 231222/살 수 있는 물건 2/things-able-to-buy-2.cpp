#include <iostream>

using namespace std;


int main() {
    int n ;
    cin >> n ;

    if (n >= 3000) {
        cout << "book" ;
    }
    else if (n>=1000) {
        cout << "mask" ;
    }
    else if (n>= 500) {
        cout << "pen" ;
    }
    else {
        cout << "no" ;
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}