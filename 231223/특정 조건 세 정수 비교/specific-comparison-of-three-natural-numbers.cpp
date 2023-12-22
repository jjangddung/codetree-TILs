#include <iostream>

using namespace std;



int main() {
    int a,b,c ;
    cin >> a >>b >>c ; 

    int minimum ;
    minimum = min(a,b) ;
    minimum = min(minimum,c) ;

    cout << (a == minimum ? 1:0) ;

    cout << " " ;


    if (a==b and b==c) {
        cout << "1";
    }
    else {
        cout << "0";
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}