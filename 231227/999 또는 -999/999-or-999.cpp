#include <iostream>

using namespace std ;



int main() {

    int mini  = 0 ;
    int maxi = 0 ;

    int N = 0 ;
    cin >> N ;
    mini = N ;
    maxi = N ;

    while (true) {
        cin >> N ;
        if (N == 999 or N == -999) {
            cout << maxi << " " << mini ;
            break;
        }
        mini = min(mini, N) ;
        maxi = max(maxi, N);

    }


    // 여기에 코드를 작성해주세요.
    return 0;
}