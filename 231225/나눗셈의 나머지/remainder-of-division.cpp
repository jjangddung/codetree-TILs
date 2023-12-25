#include <iostream>


using namespace std;



int main() {
    int a,b,c ;
    cin >> a>> b;

    int count_arr[b] = {} ;
    int arr[100] = {} ;
    int sum = 0 ;

    while (a> 1) {
        c = a% b ;
        count_arr[c] ++ ;
        a = a/b ;
    }

    for (int i = 0 ; i < b ; i ++) {
        if (count_arr[i]>= 1) {
            sum +=  count_arr[i]*count_arr[i] ;
        }
        
    }

    cout << sum ;


    // 여기에 코드를 작성해주세요.
    return 0;
}