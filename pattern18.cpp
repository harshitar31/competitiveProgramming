#include <iostream>
using namespace std;

void pattern18(int n){
    for(int i=0; i<n; i++){
        char c = 'A' + (n-i-1);
        for(int j=0;j<=i;j++){
            cout<<c;
            c++;
        }
        cout<<endl;
    }
}

int main(){
    pattern18(5);
    return 0;
}