#include <iostream>

using namespace std;



int main() {
    int a,b,c,p ;
    cin >> a>> b;

    c = a% b ;

    cout << a/b << "." ;

    
    for (int i = 0 ; i < 20 ; i ++) {
        c = 10*c;
        p = c/b ;
        c = c%b;
        cout << p ;

    }





    // 여기에 코드를 작성해주세요.
    return 0;
}