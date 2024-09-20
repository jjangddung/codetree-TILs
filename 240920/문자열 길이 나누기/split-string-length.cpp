#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    string value ;
    string word ;
    int size ;
    int two_div ;

    cin >> n ;
    for (int i = 0 ; i < n ; i ++) {
        cin >> value ;
        size = value.length() ;
        two_div = size/2 ;
        

        for (int j = 0 ; j < size ; j ++) {
            word += value[j] ;
        }
        

    }

    two_div = word.length()/2;
    
    for (int t = 0 ; t < word.length(); t ++) {
        if (t == two_div) {
            cout << endl ;
        }
        cout << word[t] ;

        
    }
    return 0;
}