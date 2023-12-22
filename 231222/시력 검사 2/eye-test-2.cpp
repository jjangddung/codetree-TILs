#include <iostream>

using namespace std;



int main() {
    double real_number ;
    cin >> real_number ;

    if (real_number>= 1.0) {
        cout << "High" ;
    }
    else if(real_number >= 0.5) {
        cout << "Middle" ;
    }
    else {
        cout << "Low" ;
    }

    // 여기에 코드를 작성해주세요.
    return 0;
}