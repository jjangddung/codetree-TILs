#include <iostream>
#include <string>

using namespace std;




int main() {
    // 여기에 코드를 작성해주세요.
    int cnt = 0 ;
    int n ;
    string arr[300] = {} ;
    string p ;

    while (true) {
        cin >> p ;

        if (p == "0") {
            break;
        }

        cnt += 1;

        arr[cnt] =  p ;

    
        
    }
    cout << cnt << endl ;

    for (int i = 1 ; i <= cnt ; i ++) {
        if (i%2 != 0) {
            cout << arr[i] << endl ;
        }
    }
    return 0;
}