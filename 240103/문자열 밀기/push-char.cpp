#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string s ;

    cin >> s;

    int k  = s.length();

    s = s.substr(1,k-1) + s.substr(0,1);
    cout << s;
    return 0;
}