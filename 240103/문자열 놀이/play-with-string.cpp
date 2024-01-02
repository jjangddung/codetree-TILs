#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string s ;
    int n ;
    cin >> s >> n;
    int x,y,z ;
    char temp ;
    char   o, p ;

    int k = s.length();

    for (int i = 0 ; i < n ; i++) {
        cin >> x  ;
        if (x == 1) {
            cin >> y >> z;

            temp = s[y-1];
            s[y-1] = s[z-1];
            s[z-1] = temp ;

            cout << s << endl ;

        }

        else {
            cin >> o >> p ;

            for (int j = 0 ; j < k ; j ++) {
                if (s[j]== o){
                    s[j]= p;
                }
            }

            cout << s << endl ;
        }
    }

    return 0;
}