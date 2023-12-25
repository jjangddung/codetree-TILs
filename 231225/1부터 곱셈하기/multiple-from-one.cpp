#include <iostream>


using namespace std;



int main() {

    int n ; 

    cin >> n;

    int proud  = 1; 


    for (int i = 1 ; i<=10 ; i ++) {
        proud *=i ;

        if (proud >= n) {
            cout << i ;
            break;
        }
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}