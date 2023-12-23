#include <iostream>
#include <string>


using namespace std;



int main() {
    string O_1, O_2, O_3 ;
    int temp_1 , temp_2 , temp_3 ;
    cin >> O_1 >>temp_1 ;
    cin >> O_2 >> temp_2 ;
    cin >> O_3 >> temp_3 ;


    int cnt = 0 ;

    if (O_1 == "Y" and temp_1 >= 37) {
        cnt +=1 ;
    }
    if (O_2 == "Y" and temp_2 >= 37) {
        cnt +=1 ;
    }
    if (O_3 == "Y" and temp_3 >= 37) {
        cnt +=1 ;
    }

    if (cnt >=2) {
        cout << "E" ;
    }
    else {
        cout << "N" ;
    }




    // 여기에 코드를 작성해주세요.
    return 0;
}