#include <iostream>

using namespace std;



int main() {
    int temp ;
    cin >> temp ;

    if (temp <0) {
        cout << "ice" ;
    }
    else if (temp >=100) {
        cout << "vapor" ;
    }

    else {
        cout << "water" ;
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}