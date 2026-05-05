#include <iostream>
using namespace std;

void pattern22(int n){
    for(int i=0;i<2*n-1;i++){
        for(int j=0;j<2*n-1;j++){
            int left =j, up=i, right=2*n-2-j, down=2*n-2-i;
            cout<<n-min(left,min(up,min(right,down)))<<" ";
        }
        cout<<endl;
    }
}

int main(){
    pattern22(4);
    return 0;
}