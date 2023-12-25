#include <iostream>

using namespace std;





int main() {

    int n ;
    int sum =  0 ;

    double k = 0 ;

    for (int i = 0 ; i < 10 ; i ++) {
        cin >> n;

        if (0<=n and n<=200) {
            sum+=n;
            k+=1;
        }

    }

    cout << fixed ;
    cout.precision(1) ;


    cout << sum << " "<<sum/k ;

    // 여기에 코드를 작성해주세요.
    return 0;
}