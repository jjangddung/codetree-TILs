#include <iostream>
#include <string>

using namespace std;




int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n; 
    int cnt = 1 ;


    for (int i = n ; i <= n*n ; i+=n) {
        for (int j = i ; j >= cnt ; j-=cnt ) {
            cout << j << " ";
        }
        cout << endl ;
        cnt +=1;
    }


    return 0;
}