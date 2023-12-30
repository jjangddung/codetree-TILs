#include <iostream>

using namespace std;




int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >>n ;

    for (int i = n ; i >= 1 ;i --) {
        for (int j = i ; j >= 1 ; j--) {
            cout <<"*";
            cout <<" ";
        }
        cout << endl ;
    }

    for (int i = 2 ; i <=n ;i ++) {
        for (int j = 1 ; j <= i ; j++) {
            cout <<"*";
            cout <<" ";
        }
        cout << endl ;
    }
    return 0;
}