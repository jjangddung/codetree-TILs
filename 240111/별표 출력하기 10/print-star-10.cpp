#include <iostream>
#include <string>

using namespace std;




int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n ;

    for (int i = 0 ; i <= 2*n-1 ; i ++) {
        if ( i % 2 != 0) {
            for (int j = 1 ; j <= n - (i-1)/2 ; j ++) {
                cout << "* ";
            }
        }

        else {
            for (int j = 1 ; j <= 1 + i/2 ; j ++) {
                cout << "* ";
            }

        }

        cout << endl ;
        
    }
    return 0;
}