/*
Given two arrays, arr[] and dep[], representing the arrival and departure times of trains at 
a station, your task is to calculate the minimum number of platforms required to ensure 
that no train has to wait. This problem assumes that the trains do not overlap in time and 
are scheduled to arrive and depart at precise times. Each train will arrive and depart at the 
exact time specified, and the goal is to minimize the number of platforms required to 
accommodate all trains simultaneously without delay.  
*/

#include <iostream>
#include <vector>

using namespace std;

void mergeSort(vector<int>& arr1, vector<int>& arr2, int left, int right);
void merge(vector<int>& arr1, vector<int>& arr2, int left, int mid, int right);

int main(){

    //TC : O(nlogn) as we are using merge sort and then traversing through the array

    vector<int> arr={900, 940, 950, 1100, 1500, 1800};
    vector<int> dept={910, 1200, 1120, 1130, 1900, 2000};

    // vector<int> arr={100, 100, 200, 400, 500};
    // vector<int> dept={200, 200, 400, 500, 600};

    // vector<int> arr={900, 1010, 1120};
    // vector<int> dept={1000, 1100, 1200};

    mergeSort(dept,arr,0,arr.size()-1);

    int i=1; int j=0; int maxPlatforms=1; int platform = 1;

    while(i<arr.size() && j<dept.size()){
        if(arr[i]<=dept[j]){ //checking if the train is arriving before last train's depature
            platform++;
            i++;
        }
        else{
            platform--;
            j++;
        }
        if (platform>maxPlatforms){
            maxPlatforms = platform;
        }
    }

    cout<<maxPlatforms<<endl;
    return 0;
}

void mergeSort(vector<int>& arr1, vector<int>& arr2, int left, int right){
    //sorting both arrays simultaneously to maintain one to one correspondance
    if (left<right){
        int mid = (left+right)/2;
        mergeSort(arr1,arr2,left,mid);
        mergeSort(arr1,arr2,mid+1,right);
        merge(arr1,arr2,left,mid,right);
    }
}

void merge(vector<int>& arr1, vector<int>& arr2, int left, int mid, int right){
    int n1 = mid - left + 1;
    int n2 = right - mid;
    vector<int> leftArr1(n1), rightArr1(n2);
    vector<int> leftArr2(n1), rightArr2(n2);

    for (int i = 0; i < n1; i++)
        leftArr1[i] = arr1[left + i];
    for (int i = 0; i < n2; i++)
        rightArr1[i] = arr1[mid + 1 + i];

    for (int i = 0; i < n1; i++)
        leftArr2[i] = arr2[left + i];
    for (int i = 0; i < n2; i++)
        rightArr2[i] = arr2[mid + 1 + i];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (leftArr1[i] <= rightArr1[j]) {
            arr1[k] = leftArr1[i];
            arr2[k] = leftArr2[i];
            i++;
        } else {
            arr1[k] = rightArr1[j];
            arr2[k] = rightArr2[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr1[k] = leftArr1[i];
        arr2[k] = leftArr2[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr1[k] = rightArr1[j];
        arr2[k] = rightArr2[j];
        j++;
        k++;
    }
}
