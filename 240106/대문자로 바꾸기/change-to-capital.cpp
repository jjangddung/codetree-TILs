#include <iostream>
#include <string>
#include <cctype>



using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    char arr[5][3] = {} ;
    char p ;
    for (int i = 0 ; i < 5 ; i ++) {
        for (int j = 0 ; j <3 ; j ++) {
            cin >> p;
            p = (char)toupper(p);
            cout << p << " " ;
            arr[i][j] = p;
            //cout << arr[i][j] ;
        }

        cout<<endl ;
    }


    return 0;
}