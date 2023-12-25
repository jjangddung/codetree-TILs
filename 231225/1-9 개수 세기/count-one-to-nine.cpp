#include <iostream>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    int n,p ;
    int cnt = 0 ;
    cin >> n ;

    int arr[n] = {} ;

    for (int i = 0 ; i < n ; i ++) {
        cin >> p ;

        arr[i] = p ;
    }

    for (int i = 1 ; i <= 9 ; i ++) {
        cnt = 0 ;
        for (int j = 0 ; j <n ; j++) {
            if (arr[j]==i) {
                cnt+= 1;
            }

        }
        cout << cnt << endl ;
    }

    return 0;
}