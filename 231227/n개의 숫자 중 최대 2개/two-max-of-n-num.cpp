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
    int old = INT_MIN ;


    for (int i = 0 ; i <n ; i ++) {
        if (maxi < arr[i]) {
            maxi = arr[i] ;
        }
        else  {
            if (old < arr[i] ) {
                old = arr[i] ;
            }
        }

    }

    cout << maxi << " " << old ;
    // 여기에 코드를 작성해주세요.
    return 0;
}