#include <iostream>

using namespace std;



int main() {
    char c ;
    int n ;
    int a_cnt = 0 ;
    int b_cnt = 0 ;
    int c_cnt = 0 ;
    int d_cnt = 0 ;
    for (int i = 0 ; i <3 ; i ++) {
        cin >> c >> n ;

        if (c == 'Y' and n >=37 ) {
            a_cnt += 1;
        }

        else if (c == 'N' and n>=37) {
            b_cnt += 1;
        }

        else if (c== 'Y' and n <37) {
            c_cnt += 1;
        }

        else if (c== 'N' and n <37) {
            d_cnt += 1;
        }

    }
    cout << a_cnt <<" " << b_cnt << " " << c_cnt <<" "<<d_cnt <<" ";

    if (a_cnt >= 2) {
        cout << "E" ;
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}