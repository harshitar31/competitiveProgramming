/*
Suppose you are given a set S={a1 ,a2,…,an} of tasks, where task ai  requires pi  units of 
processing time to complete, once it has started. You have one computer on which to run 
these tasks, and the computer can run only one task at a time. Let ci be the completion time 
of task ai, that is, the time at which task ai completes processing. Your goal is to minimize 
the average completion time, that is, to minimize 
For example, suppose there are two tasks, a1 and a2, with p1 = 3 and p2 = 5, and consider 
the schedule in which a2 runs first, followed by a1. Then c2 =5, c1 =8, and the average 
completion time is (5+8)/2=6.5.  
Implement an algorithm that schedules the tasks so as to minimize the average completion 
time. Each task must run non-preemptively, that is, once task ai starts, it must run 
continuously for pi units of time. Prove that your algorithm minimizes the average 
completion time. Show the correctness of this solution using different test cases
*/

#include <iostream>
#include <vector>

using namespace std;

void mergeSort(vector<int>& arr1, vector<int>& arr2, int left, int right);
void merge(vector<int>& arr1, vector<int>& arr2, int left, int mid, int right);
bool checkTestcase(vector<int> arr);

int main(){

    //TC: O(nlogn) as we are sorting the array and then traversing through it

    vector<int> tasks = {1, 2, 3, 4, 5};
    vector<int> burstTime = {3, 5, 1, 2, 4};

    // vector<int> tasks = {1, 2, 3, 4};
    // vector<int> burstTime = {4, 2, 3, 1};

    // vector<int> tasks = {1, 2, 3};
    // vector<int> burstTime = {10, 2, 5};

    // vector<int> tasks = {1, 2, 3, 4, 5, 6};
    // vector<int> burstTime = {8, 3, 7, 6, 2, -5};


    if(! checkTestcase(burstTime)){
        cout<<"Invalid Testcase"<<endl;
        return 0;
    }

    mergeSort(burstTime,tasks,0,burstTime.size()-1);

    cout<<"Schedule order: "<<endl;
    for(int i:tasks){
        cout<<i<<" ";
    }
    cout<<endl;

    int completionTime=0;
    for(int i=0;i<tasks.size();i++){
        //finding completion time (minimizing it) using logic from summation of natural numbers
        completionTime += (tasks.size()-i)*burstTime[i];
    }
    cout<<"Average Completion Time: "<<((float) completionTime/tasks.size());






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

bool checkTestcase(vector<int> arr){

    for(int i=0; i<arr.size(); i++){
        if(arr[i]<0){
            return false;
        }
    }
    
    return true;
}
