#include <iostream>

using namespace std;



int main() {
    int arr[10] = {} ;

    for (int i = 0 ; i < 10 ; i ++) {
        cin >> arr[i] ;
    }

    int maximum = 0 ;
    maximum = arr[0] ;

    for (int i = 0 ; i < 10 ; i ++) {
        maximum = max(arr[i],maximum) ;
        
    }

    cout << maximum ;




    // 여기에 코드를 작성해주세요.
    return 0;
}