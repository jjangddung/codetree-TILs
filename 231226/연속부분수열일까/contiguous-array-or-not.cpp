#include <iostream>
#include <algorithm>
#include <set>

using namespace std;



int main() {
    int n_1 , n_2 ;

    cin >> n_1 >> n_2 ;

    int arr_1[n_1] = {} ;
    int arr_2[n_2] = {} ;
    int new_arr = {} ;
    int cnt = 0 ;

    for (int i = 0 ; i < n_1 ; i ++) {
        cin >> arr_1[n_1];
    }

    for (int i = 0 ; i < n_2; i ++) {
        cin >> arr_2[n_2] ; 
    }

    for (int j = 0 ; j < n_1-n_2 + 1 ; j ++) {
        int new_arr[n_2] = {} ;
        for (int q = 0 ; q < n_2 ; q++){
            new_arr[q] =  arr_1[j+q] ; 
        }
        if (new_arr == arr_2) {
            cout << "Yes";
            cnt += 1;
            break;
        }



    }
    if (cnt == 0) {
        cout << "No" ;
    }
    /*
    set<int> t ;
    t = {1,2} ;
    set<int> s;
    s = {2,1} ;

    if (t == s) {
        cout << "Same!" ;
    }

    else {
        cout << "different";
    }
    */
    
    // 여기에 코드를 작성해주세요.
    return 0;
}