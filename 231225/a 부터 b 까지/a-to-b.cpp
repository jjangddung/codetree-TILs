#include <iostream>

using namespace std;



int main() {

    int a,b; 
    cin >> a>> b;

    while (a <= b) {
        cout << a << " " ;
        if (a % 2 == 0) {
            a+=3;
        }
        else {
            a*=2 ;
        }

    }
    // 여기에 코드를 작성해주세요.
    return 0;
}