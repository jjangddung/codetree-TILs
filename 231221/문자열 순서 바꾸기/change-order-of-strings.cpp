#include <iostream>
#include <string>


using namespace std;


int main() {

    string s ;
    string t ;
    string temp ;


    cin >> s ;
    cin >> t ;

    temp = s ;

    s = t;
    t = temp ;

    cout << s ;
    cout << endl ;
    cout << t;





    return 0;
}