#include <iostream>
#include <vector>

using namespace std;

int getMax(vector<int>&);
void bucketSort(vector<int>&,int);
void radixSort(vector<int>&);


int main(){
    vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    radixSort(arr);
    for(int i=0; i<arr.size(); i++){
        cout<<arr[i]<<" ";
    }
}

int getMax(vector<int>& arr){
    int max=arr[0];
    for(int i=0; i<arr.size();i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    return max;
}


void bucketSort(vector<int>& arr, int exp){

    int n=arr.size();
    vector<vector <int>> buckets(10);

    for(int i=0; i<n; i++){
        int index = (arr[i] / exp)%10;
        buckets[index].push_back(arr[i]);
    }

    int index=0;
    for(int i=0; i<10;i++){
        for(int j=0;j<buckets[i].size();j++){
            arr[index++]=buckets[i][j];
        }
    }
}

void radixSort(vector<int>& arr){
    int max=getMax(arr);
    for(int exp=1; max/exp>0;exp*=10){
        bucketSort(arr,exp);
    }

}
