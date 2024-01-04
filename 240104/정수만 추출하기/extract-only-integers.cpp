#include <iostream>
#include <string>
#include <cctype>

using namespace std;





int main() {
    // 여기에 코드를 작성해주세요.
    string a,b ;
    cin >> a>> b;

    int f = a.length();
    int s = b.length();

    for (int i  = 0 ; i < f ; i ++) {
        if (isdigit(a[i]) == 0){
            a = a.substr(0,i);
            break;
        }
    }

    for (int i  = 0 ; i < s ; i ++) {
        if (isdigit(b[i]) == 0){
            b = b.substr(0,i);
            break;
        }
    }

    cout << stoi(a) + stoi(b);
    return 0;
}