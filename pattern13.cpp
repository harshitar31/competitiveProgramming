#include <iostream>
using namespace std;

void pattern13(int n){
    int num=1;
    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            cout<<num<<" ";
            num++;
        }
        cout<<endl;
    }
}

int main(){
    pattern13(5);
    return 0;
}