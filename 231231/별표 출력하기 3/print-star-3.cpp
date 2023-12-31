#include <iostream>

using namespace std;



int main() {
    int n ;

    cin >> n ;


    for (int i = 1 ; i <= n ; i ++){
        for (int j = 1; j < i ; j++) {
            cout << "  ";

        }

        for (int k =1 ; k <= 2*(n-i)+1 ; k++){
            cout << "*";
            cout <<" ";
        }
        cout << endl ;
    }

    // 여기에 코드를 작성해주세요.
    return 0;
}