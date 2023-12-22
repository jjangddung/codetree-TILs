#include <iostream>


using namespace std;


int main() {
    int m, f ;
    cin >> m >> f ;

    if (m >= 90) {
        if(f>=90) {
            if (f>=95) {
                cout << "10000";
            }
            else {
                cout <<"50000";
            }
        }
        cout << "0";
    }

    else {
        cout <<"0";
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}