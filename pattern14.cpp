#include <iostream>
using namespace std;

void pattern14(int n){
    for(char i='A';i<'A'+n;i++){
        for(char j='A';j<=i;j++){
            cout<<j<<" ";
        }
        cout<<endl;
    }
}

int main(){
    pattern14(5);
    return 0;
}