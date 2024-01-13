#include <iostream>
#include <string>

using namespace std;


int main() {
    // 여기에 코드를 작성해주세요.
    int n ;

    cin >> n ;

    int cnt = 1;


    for (int i = 1; i <= n ; i ++) {
        for (int j = 1; j <= n ; j++) {
            cout << cnt ;
            cnt ++ ;
            if (cnt >=10) {
                cnt = 1;
            }
        }

        cout << endl ;
    }
    return 0;
}