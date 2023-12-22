#include <iostream>

using namespace std;


int main() {
    int a;
    cin >> a;

    if ((a % 2 != 0 and a%3 == 0) || (a%2 == 0 and a%5==0)) {
        cout << "true";
    } 

    else {
        cout << "false" ;
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}