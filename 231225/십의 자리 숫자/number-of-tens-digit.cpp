#include <iostream>

using namespace std;

int main() {

    int arr[100] = {} ;
    int n ;
    int count_arr[10] = {0,} ;
    int p = 0 ;

    for (int i = 0; i<= 100 ; i ++) {
        cin >> n;
        if (n == 0) {
            p = i ;
            break ;
        }
        n = n/10 ;
        arr[i] = n ;
    }

    for (int j = 0 ; j <= p ; j++) {
        count_arr[arr[j]] ++ ;
    }

    for (int k = 1 ; k <= 9 ; k ++) {
        cout << k << " - " << count_arr[k] << endl ;
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}


/*
#include <iostream>
using namespace std;

int main() {

	int arr[10];
	int count_arr[7] = { 0, };

	for (int i = 0; i < 10; i++) {
		cin >> arr[i];
	}

	// 개수 세기
	for (int i = 0; i < 10; i++) {
		count_arr[arr[i]]++;
	}

	// 개수 출력
	for (int i = 1; i < 7; i++) {
		cout << "숫자 " << i << " - " << count_arr[i] << "번" << endl;
	}

	return 0;

}
*/