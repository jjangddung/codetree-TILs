#include <iostream>

using namespace std;




int main() {

    int n ;
    cin >> n ;

    int cnt_1 = 0 ;
    int cnt_2 = 0 ;    
    int cnt_3 = 0 ;


    for (int i = 1 ; i <= n ; i++) {
        if (i%2 == 0 and (i%3 != 0 and i%12 != 0)) {
            cnt_1 +=1 ;

        }

        else if (i%3 == 0 and i % 12 != 0) {
            cnt_2 += 1;
        }
        if (i % 12 == 0) {
            cnt_3 += 1;
        }

       
    }
    cout << cnt_1 <<  " " << cnt_2 << " " << cnt_3 ;
    // 여기에 코드를 작성해주세요.
    return 0;
}