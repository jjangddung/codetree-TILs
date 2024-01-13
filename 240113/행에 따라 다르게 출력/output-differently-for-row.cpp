#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n ;
    int cnt = 0;


    for (int i = 1 ; i <= n ; i ++) {
        for (int j =1 ; j <=n ; j ++) {
            if (i % 2 != 0) {
                cnt ++;
                cout << cnt << " " ;
            
            }
            else {
                cnt +=2;
                cout << cnt << " " ;
            }

        }
        cout << endl ;
    }
    return 0;
}