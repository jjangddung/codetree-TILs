#include <iostream> 

using namespace std;



int main() {

    int N ;
    cin >>  N ;

    int cnt = 0 ;

    int arr[N] = {} ;

    for (int i = 0 ; i  < N ; i ++) {
        cin >> arr[i] ;
    }

    int minimum = arr[0] ;

    for (int i = 0 ; i < N ; i ++) {
        minimum = min(arr[i], minimum);
    }

    cout << minimum << " ";

    for (int j = 0 ; j < N  ; j ++) {
        if (arr[j] == minimum) {
            cnt += 1;
        }
    }

    cout << cnt ;
    // 여기에 코드를 작성해주세요.
    return 0;
}