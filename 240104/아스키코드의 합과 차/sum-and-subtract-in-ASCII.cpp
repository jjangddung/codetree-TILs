#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    char a,b ;
    cin >> a >> b;

    int t = (int)a ;
    int q = (int)b ;

    cout << t + q << " " ;

    cout << ((t>=q) ? t-q : q-t) ;
    return 0;
}