#include <iostream>
#include <string>
using namespace std;



int main() {
    string alpha ;
    cin >> alpha ;


    if (alpha == "S") {
        cout << "Superior" ;
    }

    else if(alpha == "A") {
        cout << "Excellent" ;
    }
    else if(alpha == "B") {
        cout << "Good" ;
    }
    else if(alpha == "C") {
        cout << "Usually" ;
    }
    else if(alpha == "D") {
        cout << "Effort" ;
    }
    else  {
        cout << "Failure" ;
    }

    // 여기에 코드를 작성해주세요.
    return 0;
}