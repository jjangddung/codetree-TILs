#include <iostream>

using namespace  std;




int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >>n ;

    for (int i = 1 ; i <=n ; i ++) {

        for (int k = 1; k < i ; k++) {
            cout << "  ";
        }




        for (int j = 1; j <=2*(n-i)+1 ; j++) {
            cout << "*";
            cout <<" ";
        }
        cout << endl ;

    }

    for (int i = 2 ; i <=n ; i ++) {

        for (int k = 1; k <= n-i ; k++) {
            cout << "  ";
        }




        for (int j = 1; j <=2*i-1 ; j++) {
            cout << "*";
            cout <<" ";
        }
        cout << endl ;

    }


    return 0;
}