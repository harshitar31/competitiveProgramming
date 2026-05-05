/*
A Farmer has to arrange a row of n sack piles on the farm. The ith pile contains ai sack. 
Every day, he can choose to move one sack from any pile to an adjacent pile. Formally, 
in one day he can choose any two indices i and j (1≤i, j≤n) such that |i−j|=1 and ai>0 and 
apply: ai=ai−1, aj=aj+1. He may also decide to not do anything on some days because he 
is lazy. He wants to maximize the number of sack in pile 1 (i.e. to maximize a1), and he 
only has d days to do so. Help him find the maximum number of sack that may be in pile 
1 if he acts optimally! 

The input consists of multiple test cases. The first line contains an integer t (1≤t≤100)  — 
the number of test cases. Next 2t lines contain a description of test cases  — two lines per 
test case. 
The first line of each test case contains integers n and d (1≤n, d≤100) — the number of 
sack piles and the number of days, respectively. 
The second line of each test case contains n integers a1, a2,…,an (0≤ai≤100)  — the 
number of sack in each pile. 

For each test case, output one integer: the maximum number of sack that may be in pile 1 
after d days if farmer acts optimally. 
*/

#include <iostream>
#include <vector>

using namespace std;

bool checkTestcase(int n, int d, vector<int> arr);

int main(){

    //TC: O(n) as we are traversing through the array once

    // 3 
    // 4 5 
    // 1 0 3 2 
    // 2 2 
    // 100 1 
    // 1 8 
    // 0 


    // 1
    // 5 5
    // 0 1 2 3 4


    // 3
    // 4 6
    // 3 2 1 4
    // 3 3
    // 10 10 10
    // 2 5
    // 1 -1



    int testcases;
    cin>>testcases;
    while(testcases--){
        int n,d;
        cin>>n>>d;
        vector<int> arr(n);
        for(int i=0; i<n; i++){
            cin>>arr[i];
        }

        if(! checkTestcase(n,d,arr)){
            cout<<"Invalid Testcase"<<endl;
            return 0;
        }

        for(int i=1; i<n; i++){
            if(d>=arr[i]*i){  //checking if it is possible to move all sacks from the next pile to first pile
                arr[0]+=arr[i];
                d-=arr[i]*i;
            }
            else{
                arr[0]+=(d/i);
                break;
            }
        }
        cout<<arr[0]<<endl;
    }



    return 0;
}

bool checkTestcase(int n, int d, vector<int> arr){
    if(n<1){
        return false;
    }
    else if(d>100){
        return false;
    }
    else{
        for(int i=0; i<n; i++){
            if(arr[i]>100 || arr[i]<0){
                return false;
            }
        }
    }
    return true;
}
