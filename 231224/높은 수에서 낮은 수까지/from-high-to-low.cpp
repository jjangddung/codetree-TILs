#include <iostream>

using namespace std;



int main() {

    int a,b, maximum,minimum ;
    cin >> a >>b ;
    maximum = max(a,b);
    minimum = min(a,b) ;

    for (int i = maximum ; i >= minimum ; i--) {
        cout << i << " ";

    }
    // 여기에 코드를 작성해주세요.
    return 0;
}