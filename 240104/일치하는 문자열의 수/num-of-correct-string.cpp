#include <iostream>
#include <string>
#include <cctype>

using namespace std;




int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    string s ;
    cin >> n  >> s;

    string str;
    int cnt = 0 ;

    for (int i = 0 ; i < n ; i ++) {
        cin >> str;
        if (str==s) {
            cnt+=1;
        }
    }

    cout << cnt ;
    return 0;
}