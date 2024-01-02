#include <iostream>
#include <string>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string str ;

    cin >> str ;

    int k  = str.length();
    int position ;


    while (k > 1) {
        cin >> position ;

        if (position >= k-1) {
            str.erase(k-1,1);
        }
        else {

            str.erase(position,1);
        }


        cout << str  << endl ;
        k = str.length();

    }

    return 0;
}