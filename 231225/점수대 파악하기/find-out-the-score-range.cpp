#include <iostream>

using namespace std;



int main() {
    int arr[100] = {} ;

    int count_arr[11] = {0,} ;

    for (int i = 0 ; i <= 100 ; i ++) {
        cin  >> arr[i] ;

        if (arr[i]== 0) {
            break ;
        }

    }

    for (int j = 0 ; j <= 100 ; j++) {
        count_arr[arr[j]/10]++ ;
    }

    for (int k = 10; k >= 1 ; k--) {
        cout << 10*k <<" - " << count_arr[k] <<endl ;
    }

    
    // 여기에 코드를 작성해주세요.
    return 0;
}