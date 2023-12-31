#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    int cnt = 0 ;
    string str ;
    cin >> str  ;
    string que;
    cin >> que ;

    int len = str.length();
    int q_len = que.length();

    for (int i = 0 ; i < len - q_len +1 ;i++){
        if (str.substr(i,q_len)==que) {
            cnt+=1;
        }
    }

    cout << cnt ;

    return 0;
}