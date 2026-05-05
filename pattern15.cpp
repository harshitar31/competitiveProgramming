#include <iostream>
using namespace std;

void pattern15(int n){
    for(char i=0;i<n;i++){
        char c='A';
        for(int j=0;j<n-i;j++){
            cout<<c<<" ";
            c++;
        }
        cout<<endl;
    }
}

int main(){
    pattern15(5);
    return 0;
}