#include <iostream>

using namespace std;




int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >>n ;

    for (int i = 1 ; i <= n ; i ++) {
        for (int j = 1 ; j <= n+1-i ; j ++) {
            cout << i << " * " << j << " = " << i*j  ;
            if (j == n+1-i) {
                cout << endl ;
            }
            else {
                cout << " / ";
            }
        }
    }
    return 0;
}