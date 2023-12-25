#include <iostream>

using namespace std;



int main() {

    int arr[10] = {} ;
    int n ;
    int cnt = 0 ;


    for (int i = 0 ; i < 10 ; i ++) {
        cin >> n ;
        arr[i] = n ;

    }

    for (int j = 1 ; j <=6 ; j++) {
        cnt = 0 ;
        for (int i = 0 ; i < 10 ; i ++) {
            if (arr[i]== j) {
                cnt +=1 ;
            }
        }
        cout << j <<" - " << cnt << endl ;
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}