#include <iostream>

using namespace std;




int main() {
    int n ;
    cin >> n ;
    int cnt = 0 ;

    for (int i = 1 ; i <= n; i++) {
        if (i % 2 == 0 or i %3 == 0 or i % 5 ==0 ){
            continue ;
        }

        cnt += 1;

    }

    cout << cnt ;
    // 여기에 코드를 작성해주세요.
    return 0;
}