#include <iostream>


using namespace std;



int main() {
    int a,b ;

    cin >> a >> b;

    int result = 0 ;

    for (int i = a ; i <= b ; i++) {
        
        if (i%5 ==0) {
            result +=i ;
        }
    }

    cout << result ;
    // 여기에 코드를 작성해주세요.
    return 0;
}