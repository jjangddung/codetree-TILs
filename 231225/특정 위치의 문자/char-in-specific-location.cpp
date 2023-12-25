#include <iostream>

using namespace std;



int main() {

    char word[6] = {'L','E','B','R','O','S'} ;

    char w ;
    cin >> w ;
    int idx = -1 ;


    for (int i = 0 ; i < 6 ; i ++) {
        if (word[i]== w) {
            cout << i ;
            idx  = i ;
        }
    }

    if (idx == -1) {
        cout << "None" ;
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}