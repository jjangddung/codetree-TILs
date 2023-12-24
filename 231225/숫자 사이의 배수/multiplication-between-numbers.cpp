#include <iostream>

using namespace std;



int main() {

    int a, b ;

    int result = 0 ;
    double avg;
    double cnt = 0 ;

    cin >> a >> b ;

    for (int i = a ; i <=b ; i++) {
        if (i % 5== 0 or i % 7 == 0) {
            result += i ;
            cnt += 1;
        }

        


    }
    cout << fixed ;
    cout.precision(1) ;
    avg = result /cnt ;
    cout << result << " " << avg ;
    // 여기에 코드를 작성해주세요.
    return 0;
}