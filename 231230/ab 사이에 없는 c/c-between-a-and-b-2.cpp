#include <iostream>


using namespace std;



int main() {

    int a,b,c ;
    int cnt = 0 ;

    cin >> a>> b>> c;

    for (int i = a;  i <= b ;i ++) {
        if (i%c == 0) {
            cout << "NO" ;
            cnt +=1 ;
        }
    }

    if (cnt != 0) {
        cout << "YES" ;
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}