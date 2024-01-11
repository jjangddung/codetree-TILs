#include <iostream>
#include <string>

using namespace std;




int main() {
    // 여기에 코드를 작성해주세요.
    int n ;

    cin >> n ;
    int cnt = 0 ;



    for (int i =  1 ; i <= n ; i ++) {
        cnt = n - i ;

        for (int k = 1 ; k <= n-i ; k ++) {
            cout << " ";
        }
        for (int j  = 1 ; j <= 2*i-1 ; j ++) {

            cout << "*";
            
        }

        cout << endl ;

    }

    for ( int i = n-1 ; i >= 1 ; i --) {
        for (int k = 1 ; k <= n-i ; k ++) {
            cout << " ";
        }

        for (int j  = 1 ; j <= 2*i-1 ; j ++) {

            cout << "*";
            
        }

        cout << endl ;

    }
    return 0;
}