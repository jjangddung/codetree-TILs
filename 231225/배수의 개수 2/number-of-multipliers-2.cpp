#include <iostream>

using namespace std;



int main() {
    int n, cnt ;
    cnt = 0 ;
    for (int i = 0 ; i < 10 ; i++) {
        cin >> n ;
        if (n% 2 != 0) {
            cnt +=1 ;

        }

    }

    cout << cnt ;
    // 여기에 코드를 작성해주세요.
    return 0;
}