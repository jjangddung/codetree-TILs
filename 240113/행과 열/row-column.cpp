#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    int n, m ;

    cin >> n >> m ;

    for (int i = 1;  i <= 4 ; i ++) {
        for (int j = i ; j <= i*m ; j += i) {
            cout << j << " ";
        }
        cout << endl ;
    }
    return 0;
}