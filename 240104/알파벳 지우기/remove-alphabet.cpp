#include <iostream>
#include <string>
#include <cctype>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    string A,B ;
    cin >> A >> B ;

    int A_len = A.length();
    int B_len = B.length();
    string C ;
    string D ;


    for (int i = 0 ; i < A_len ; i ++) {
        if (isdigit(A[i]) != 0) {
            C += A[i] ;
        }
    }

    for (int i = 0 ; i < B_len ; i ++) {
        if (isdigit(B[i]) != 0) {
            D += B[i] ;
        }
    }

    cout << stoi(C) + stoi(D) ;
    return 0;
}