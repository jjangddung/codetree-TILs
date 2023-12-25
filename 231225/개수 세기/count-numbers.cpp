#include <iostream>

using namespace std;



int main() {
    int n , m ; 
    cin >> n >> m;

    int arr[n] = {} ;

    int g = 0 ;
    int cnt = 0 ;

    for (int i = 0 ; i < n ; i ++) {
        cin >> g;
        arr[i] = g ;
        
    }

    for (int i = 0 ; i < n ; i ++) {
        if (arr[i]== m) {
            cnt ++ ;
        }
    }

    cout << cnt ;
    // 여기에 코드를 작성해주세요.
    return 0;
}