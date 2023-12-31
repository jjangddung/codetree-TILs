#include <iostream>
#include <string>

using namespace std;





int main() {
    string str ;
    cin >>str ;
    bool first = false ;
    bool second = false ;


    int len = str.length() ;

    for (int i = 0 ; i <  len - 1 ;i ++) {
        if(str.substr(i,2)== "ee"){
            first = true ;
        }

        if (str.substr(i,2) == "ab"){
            second = true ;


        }
    }

    if (first == true) {
        cout << "Yes";
    }

    else {
        cout << "No" ;
    }

    cout << " ";

    if (second == true) {
        cout << "Yes";
    }

    else {
        cout << "No" ;
    }


    // 여기에 코드를 작성해주세요.
    return 0;
}