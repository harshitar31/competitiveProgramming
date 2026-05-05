#include <iostream>
using namespace std;

void selectionSort(int[],int);

int main(){
    int n;
    cout<<"Enter size n: ";
    cin>>n;

    int arr[n];
    for (int i=0; i<n; i++) {
        cin>>arr[i];
    }
    selectionSort(arr,n);
    cout<<"Sorted array: \n";
    for (int i=0; i<n; i++) {
        cout<<arr[i]<<" ";
    }


    return 0;
}

void selectionSort(int arr[], int n){

    for(int i=0;i<n;i++){
        int mini=i;
        for (int j=i; j<n; j++) {
            if(arr[j]<arr[mini]){
                mini=j;
            }
        }
        int temp=arr[i];
        arr[i]=arr[mini];
        arr[mini]=temp;
    }


}
