#include <iostream>
#include <string>


using namespace std;



int main() {
    int n, q ;

    cin >> n >> q ;

    int arr[n] = {} ;
    int q_arr[3] = {};

    
    for (int i = 0 ; i < n ; i ++) {
        cin >> arr[i] ;
    }

    for (int i = 0 ; i < q ; i ++) {
        int q_arr[3] = {0,0,0} ;
        cin >> q_arr[0] ;

        if (q_arr[0]== 1) {
            cin >> q_arr[1] ;
            cout << arr[q_arr[1]-1] << endl ;
            }
        
        else if (q_arr[0]== 2) {
            cin >> q_arr[1];
            for (int k = 0 ; k <n ; k ++) {
                if (arr[k]== q_arr[1]) {
                    cout << k+1  << endl ;
                    break;
                }
            }
        }

        else {
            cin >>q_arr[1] >>q_arr[2] ;
            for (int w = q_arr[1]-1 ; w <= q_arr[2]-1 ; w++) {
                cout <<arr[w] << " ";
            }
            cout << endl ;
        }
    }
        
    

    // 여기에 코드를 작성해주세요.
    return 0;
}