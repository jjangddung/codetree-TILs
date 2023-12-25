#include <iostream>

using namespace std;



int main() {
    int n ;
    int p ;
    int sum = 0 ;
    double avg;

    cin >> n;



    for (int i = 0 ; i < n ; i ++) {
        cin >> p;
        sum += p;

        
    }

    cout <<fixed ;

    cout.precision(1) ;

    avg = double(sum) / n ;
    

    cout << sum << " " << avg;
    // 여기에 코드를 작성해주세요.
    return 0;
}