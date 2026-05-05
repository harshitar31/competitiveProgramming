#include <iostream>
using namespace std;

void pattern16(int n){
    for(int i=0; i<n;i++){
        char c = 'A' + i;
        for(int j=0;j<=i;j++){
            cout<<c<<" ";
        }
        cout<<endl;
    }
}

int main(){
    pattern16(5);
    return 0;
}