#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n;
    char p = 'A' ;


    for (int i = 1 ; i <= n ;i++){
        for (int j =1 ; j <= i ; j ++) {
            cout << p ;
            if (p == 'Z') {
                p = 'A';
            }
            else {
                p++;
            }
            
        }
        cout << endl ;
    }
    return 0;
}