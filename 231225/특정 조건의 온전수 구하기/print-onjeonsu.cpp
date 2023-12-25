#include <iostream>

using namespace std;



int main() {

    int n ;

    cin >> n; 

    for (int i =1 ; i <= n ; i ++) {
        if (i%2 == 0) {
            continue;
        }

        else if (i == 5) {
            continue ;
        }

        else if (i> 10 and (i%10)==5) {
            continue;
        }

        else if( i > 100 and (i%100) == 5) {
            continue ;
        }

        else if (i% 3 == 0 and i%9 != 0) {
            continue ;
        }

        cout << i << " " ;

    }

    // 여기에 코드를 작성해주세요.
    return 0;
}