#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n;

    int cnt = 1;


    for (int i= 1; i <=n ; i ++) {
        for (int j = 1; j <=n ; j ++) {
            if (i % 2 != 0) {
                if (i !=1 and j==1) {
                    cnt = cnt + n+1;
                }
                cout << cnt << " " ;
                cnt ++ ;
            }
            else {
                if (j==1) {
                    cnt = cnt +n -1;
                }
                cout << cnt << " ";
                cnt -- ;

            }
        }
        cout << endl ;

    }
}