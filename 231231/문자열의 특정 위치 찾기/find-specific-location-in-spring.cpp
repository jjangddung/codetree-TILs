#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string str ;
    char p ;

    cin >> str >> p ;

    int k = str.length();


    for (int i = 0 ; i <k -1 ; i ++) {
        if (str[i] != p){
            continue;
        }

        cout << i ;
        break;
    }

    return 0;
}