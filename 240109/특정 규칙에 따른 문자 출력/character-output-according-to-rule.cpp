#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요
    int n;
    cin >> n;
    int cnt=0;

    for (int i=1; i<=n; i++){
        for(int j = 1 ;j<=n-i; j++){
            cout <<"  ";
            cnt+=1;
        }
        for(int k= 1; k<= n-cnt; k++){
            cout<<"@ ";
        }
        cout << endl;
        cnt = 0;
    }
    for (int i = 1; i<=n-1 ; i ++){
        for(int j = n-1 ; j>= i ; j--){
            cout<<"@ ";
        }
        cout<< endl;
    }



    

    

    return 0;
}