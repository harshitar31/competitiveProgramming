#include <iostream>
using namespace std;

void bubbleSort(int[],int);

int main() {
    int n;
    cout<<"Enter size n: ";
    cin>>n;

    int arr[n];
    for (int i=0; i<n; i++) {
        cin>>arr[i];
    }
    bubbleSort(arr,n);
    cout<<"Sorted array: \n";
    for (int i=0; i<n; i++) {
        cout<<arr[i]<<" ";
    }

    return 0;
}

void bubbleSort(int arr[], int n){
    bool swapped = false;
    int temp;
    for(int i=0; i<n-1; i++){
        swapped=false;
        for (int j=0; j<n-i-1; j++){
            if (arr[j]>arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1]=temp;

                swapped=true;
            }
        }
        if (!swapped){
            return;
        }
    }
}
