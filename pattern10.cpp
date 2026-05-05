#include <iostream>
using namespace std;

void pattern10(int n){
    for(int i=0;i<=2*n-1;i++){
        int s=i;
        if(i>n) s=2*n-i;
        for(int j=0;j<s;j++){
            cout<<"*";
        }
        cout<<endl;
    }
}

int main(){
    pattern10(5);
    return 0;
}