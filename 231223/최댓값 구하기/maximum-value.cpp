#include <iostream>

using namespace std;


int main() {
    int a,b,c, maximum ;

    cin >> a>> b>> c;

    maximum = max(a,b) ;
    maximum = max(maximum,c) ;

    cout << maximum ;
    // 여기에 코드를 작성해주세요.
    return 0;
}