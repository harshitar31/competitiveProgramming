#include <iostream>
#include <vector>

using namespace std;

void bucketSort(vector<float>& arr);
void insertionSort(vector<float>& arr);

int main(){
    vector<float> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    bucketSort(arr);
    for(int i=0; i<arr.size(); i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}

void bucketSort(vector<float>& arr){
    int n = arr.size();
    if (n<=1) return;

    float max=arr[0];
    for(int i=0; i<arr.size();i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }

    vector<vector <float>> buckets(n);

    for(int i=0; i<n; i++){
        int index = n * arr[i] / (max + 1);
        buckets[index].push_back(arr[i]);
    }

    for(int i=0; i<n; i++){
        insertionSort(buckets[i]);
    }

    int index=0;
    for(int i=0; i<n;i++){
        for(int j=0;j<buckets[i].size();j++){
            arr[index++]=buckets[i][j];
        }
    }

}

void insertionSort(vector<float>& arr){
    int n=arr.size();
     for(int i=0;i<n;i++){
        int j=i-1;
        float key=arr[i];
        while(j>=0 && arr[j]>key){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=key;
    }
}
