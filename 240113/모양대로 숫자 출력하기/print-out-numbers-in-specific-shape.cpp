#include <iostream>
#include <string>

using namespace std;




int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n;


    for (int i = n ; i >= 1; i-- ) {
        for (int k = 1; k<= n-i ; k++) {
                cout << "  ";
            }
        for (int j = i ; j>= 1 ; j--) {
            cout << j << " ";
        }
        cout << endl ;
    }
    return 0;
}