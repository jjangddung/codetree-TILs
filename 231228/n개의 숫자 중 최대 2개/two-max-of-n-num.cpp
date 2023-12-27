#include <iostream>
#include <climits>

using namespace std;



int main() {
    int n = 0 ;
    cin >> n ;
    
    int arr[n] = {} ;

    for (int i= 0 ; i < n ; i ++){
        cin >> arr[i] ;
    } 

    int maxi = arr[0] ;
    int ne = INT_MIN;


    for (int i = 0 ; i <n ; i ++) {
        if (maxi < arr[i]) {
            maxi = arr[i] ;
        }
    }

    cout << maxi <<" ";
    int cnt = 0 ;

    for (int i = 0 ; i < n ; i ++) {
        if (maxi == arr[i]) {
            cnt += 1;
        }
    }

    if (cnt>=2) {
        cout << maxi ;
    }

    else {
        for(int i = 0 ; i < n ; i ++) {
            if (ne <arr[i] and arr[i] < maxi ) {
                ne = arr[i];
            }

        }

        cout << ne ;

    }

    // 여기에 코드를 작성해주세요.
    return 0;
}