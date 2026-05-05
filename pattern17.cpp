#include <iostream>
using namespace std;

void pattern17(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i-1;j++){
            cout<<" ";
        }
        char c='A';
        for(int j=1;j<=2*i+1;j++){
            cout << c;
            if(j<=(2*i+1)/2) c++;
            else c--;  
        }
        for(int j=0;j<n-i-1;j++){
            cout<<" ";
        }
        cout<<endl;
    }
}

int main(){
    pattern17(5);
    return 0;
}