#include <iostream>

using namespace std;



int main() {
    int a_m, a_e ;
    int b_m, b_e ;

    cin >>a_m >>a_e >>b_m >> b_e ;

    if (a_m > b_m) {
        cout << "A" ;
    }
    else if (a_m == b_m) {
        if (a_e > b_e) {
            cout << "A";
        }
        else {
            cout << "B" ;
        }
    }

    else {
        cout << "B";
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}