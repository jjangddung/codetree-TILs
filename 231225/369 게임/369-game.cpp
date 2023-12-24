#include <iostream>
#include <string>



using namespace std;


int main() {
    int n,t,g ;
    cin >> n;
    string str ;


    for (int i = 1 ; i<= n ; i ++) {
        g = i/10 ;
        t = i%10 ;
        if (i%3 == 0) {
            cout << 0 << " ";
        }

        else {
            if (g==3 or g==6 or  g== 9  or t % 3== 0) {
                cout << 0 << " ";
            }
            else {
                cout <<i << " ";
            }


        }
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}