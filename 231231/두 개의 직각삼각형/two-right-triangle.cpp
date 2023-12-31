#include <iostream>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n ;


    for (int i = 1 ; i <=n ; i++) {
        for (int j = 1 ; j <=n-i+1; j++){
            cout <<"*";
        }

        for (int k = 1; k <=2*(i-1); k++){
            cout <<" ";

        }

        for (int j = 1 ; j <=n-i+1; j++){
            cout <<"*";
        }
        



        cout << endl ;
    }
    return 0;
}