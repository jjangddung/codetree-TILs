#include <iostream>

using namespace std;



int main() {

    int arr[10] = {} ;

    for (int i = 0 ; i < 10 ; i ++) {
        cin >> arr[i];
    }

    int mini = -500 ; 
    int max = 1000 ;
    int chai = 0 ;



    for (int i = 0 ; i < 10 ; i++) {
        if (arr[i] < 500 and mini < arr[i]) {
            mini = arr[i];
        }

        if (arr[i]>500 and arr[i]< max) {
            max = arr[i];
        }

    }

    cout << mini << " " << max ;
    // 여기에 코드를 작성해주세요.
    return 0;
}