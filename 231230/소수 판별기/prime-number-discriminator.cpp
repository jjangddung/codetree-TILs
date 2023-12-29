#include <iostream>

using namespace std;




int main() {

    int n ;
    cin >> n ;
    int cnt = 0;

    for (int i = 2 ; i < n ; i ++) {
         if (n % i == 0) {
            cout << "C";
            cnt = 1;
            break;

         }
    }

    if (cnt==0) {
        cout << "P" ;
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}