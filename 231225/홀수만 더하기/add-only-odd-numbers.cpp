#include <iostream>

using namespace std;



int main() {

    int n ;
    cin >> n ;
    int result = 0 ;
    int q ;

    for (int  i = 0 ; i < n ; i++) {
        cin >> q ;
        if (q% 2 != 0 and q % 3== 0) {
            result += q;
            
        }

    }

    cout << result ;
    // 여기에 코드를 작성해주세요.
    return 0;
}