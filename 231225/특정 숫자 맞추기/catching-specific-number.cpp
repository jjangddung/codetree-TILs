#include <iostream>

using namespace std;




int main() {
    int n ;

    while (true) {
        cin >> n ;
        if (n > 25) {
            cout << "Lower" <<endl ;
        }
        else if (n<25) {
            cout << "Higher" << endl ;
        }

        else {
            cout <<"Good";
            break;
        } 
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}