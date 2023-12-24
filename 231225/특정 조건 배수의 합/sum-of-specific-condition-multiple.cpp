#include <iostream>


using namespace std;



int main() {
    int a,b,min,max ;

    cin >> a >> b;

    int result = 0 ;

    if (a< b) {
        min = a;
        max = b;
    }
    else {
        min = b ;
        max = a;
    }

    for (int i = min ; i <= max ; i++) {
        
        if (i%5 ==0) {
            result +=i ;
        }
    }

    cout << result ;
    return 0;
}