#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string prob ;
    string solv ;
    cin >> prob >> solv ;

    int len = prob.length();
    int solv_len = solv.length();

    for (int i = 0 ; i < len - solv_len +1 ; i ++) {
        if (prob.substr(i,solv_len) == solv) {
            cout << i ;
            break;
        }
    }
    return 0;
}