#include <iostream>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n ;

    for (int i = 1 ; i <= n ; i++) {
        for (int j = 1 ; j <= n-i ; j++){
            cout << "  ";
        }

        for (int k = 1; k <= 2*i-1 ; k++) {
            cout <<"*";
            cout <<" ";
        }

        cout << endl ;
    }
    return 0;
}