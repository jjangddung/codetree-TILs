#include <iostream>

using namespace std;



int main() {

    int cnt_1 = 0 ;
    int cnt_2 = 0 ;
    int n ;

    for (int i = 0 ; i < 10 ; i++) {
        cin >> n ;
        if (n % 3 == 0) {
            cnt_1 +=1 ;
        }
        if (n%5 ==0) {
            cnt_2 +=1 ;
        }
      
    }
    cout << cnt_1 <<" " <<cnt_2 ;
    // 여기에 코드를 작성해주세요.
    return 0;
}