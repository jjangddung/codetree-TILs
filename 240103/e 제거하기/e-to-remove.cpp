#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string s ;
    cin >> s;

    int k = s.length();

    for (int i = 0 ; i < k ; i++) {
        if (s[i]== 'e') {
            s.erase(i,1);
            break;
        }
    }

    cout << s ;
    return 0;
}