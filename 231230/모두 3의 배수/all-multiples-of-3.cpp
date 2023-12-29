#include <iostream>


using namespace std;




int main() {

    int k = 0 ;

    for (int i = 0 ; i<5 ; i ++) {
        cin >> k ;

        if (k%3 == 0){
            if (i < 4){
            continue ;
            }
            else {
                cout << 1 ;
            }
        } 

        else {
            cout << 0 ;
            break ;
        }
        
    }
    return 0;
}