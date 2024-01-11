#include <iostream>
#include <string>

using namespace std;





int main() {
    // 여기에 코드를 작성해주세요.
    int a,b ;
    int cnt = 1 ;

    cin >> a>> b;
    for (int j = 1 ; j  <= 9 ; j ++) {
        for (int i = b ; i >= a ; i --) {
            if (i%2 == 0) {
                cout << i << " * " <<j << " = " << i*j ;
                if ( i > a) {
                    cout << " / ";

                }
            
            }
        }
        cout << endl ;
    }
    return 0;
}