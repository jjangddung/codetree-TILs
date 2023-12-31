#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.

    string A ;
    string B ;

    cin >> A >> B ;
    
    string C ;
    C =  A+ B ;
    string D ;
    D = B+ A ;
    if (C==D) {
        cout << "true";
    }
    else {
        cout <<"false";
    }
    return 0;
}