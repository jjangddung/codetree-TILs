#include <iostream>
#include <string>

using namespace std ;


int main() {
    // 여기에 코드를 작성해주세요.
    string  A ,B ;
    cin >>  A >> B ;

    string first , second ;
    
    first  = A + B ;
    second = B + A ;

    int f = stoi(first) + stoi(second) ;

    cout << f;

    return 0;
}