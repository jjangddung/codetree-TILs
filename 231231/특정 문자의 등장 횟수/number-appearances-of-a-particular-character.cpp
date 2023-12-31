#include <iostream>
#include <string>



using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string str ;
    cin >> str ;
    int k = str.length();

    int cnt_1 = 0 ;
    int cnt_2 = 0 ;

    for (int i = 0 ; i < k-1 ; i ++) {
        if (str.substr(i,2)== "ee") {
            cnt_1 +=1 ;

        }

        if (str.substr(i,2)== "eb") {
            cnt_2 +=1 ;

        }
    }

    cout << cnt_1 << " " << cnt_2 ;
    return 0;
}