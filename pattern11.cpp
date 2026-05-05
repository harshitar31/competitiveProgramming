#include <iostream>
using namespace std;

void pattern11(int n){
    int c=1;
    for(int i=0;i<n;i++){
        if(i%2==0) c=1;
        else c=0;
        for(int j=0;j<=i;j++){
            cout<<c<<" ";
            c=1-c;
        }
        cout<<endl;
    }
}

int main(){
    pattern11(5);
    return 0;
}