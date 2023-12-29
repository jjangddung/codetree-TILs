#include <iostream>

using namespace std;




int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n;

    int cnt = 0 ;

    while (true) {
        if (n==1) {
            cout << cnt ;
            break;

        }

        if (n % 2 == 0) {
            cnt +=1 ;
            n /= 2 ;
        }

        else {
            cnt += 1;
            n = 3*n +1 ;
        }
    }

    return 0;
}