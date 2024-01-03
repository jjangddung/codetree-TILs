#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string s ;
    int q ;
    int a ;

    cin >> s;
    cin >> q ;

    int len = s.length();


    for (int i = 0 ; i < q ; i ++) {
        cin >> a;

        if (a==1){
            s = s.substr(1,len-1) + s.substr(0,1) ;
            cout <<s << endl ;


        }

        else if (a == 2) {
            s = s.substr(len-1,1) + s.substr(0,len-1);
            cout << s << endl ;

        }

        else {
            for (int j = len -1 ; j >=0 ; j -- ){
                cout << s[j];
            }
            cout<< endl ;
        }
    }
    return 0;
}