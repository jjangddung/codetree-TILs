#include <iostream>

using namespace std;



int main() {

    int a,b,c, minimum ;
    cin >> a >> b>> c;
    minimum = a ;

    if (a <= b and a<= c) {
        cout << a;
    } 
    else if (b <= a and b <= c) {
        cout << b;
    }
    
    else {
        cout << c;
    }
    return 0;
}