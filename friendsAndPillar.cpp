/*
You and your friend are at opposite ends of a row of tall pillars placed along a straight road. 
The road is not safe due to strong winds, and you both need to find the safest shelter to stay 
protected from the elements. The only way to find shelter is by using two pillars to form a 
protective barrier. 
Each pillar has a height and can protect from the wind. The more distance between the two 
pillars and the taller they are, the more sheltered you and your friend will be. You and your 
friend want to find two pillars that will give the maximum protection (i.e., the maximum 
area of safety) between you both. 
The safety between two pillars depends on their height and the distance between them. The 
taller the pillars, the safer you will be. Your objective is to choose the safest pair of pillars 
that give you the maximum area of protection. 
Input: 
An integer array height of length n representing the heights of the pillars, where the i-th 
pillar stands at position i and has a height of height[i]. 
Output: 
The maximum protection (area) that can be provided between any two pillars. 
*/

#include <iostream>
#include <vector>

using namespace std;

bool checkTestcase(vector<int> arr);

int main(){

    //TC : O(n) as we are traversing through the array once with 2 pointer variables 

    vector<int> height = {1,8,6,2,5,4,8,3,7};

    // vector<int> height = {4, 3, 2, 1, 4};

    // vector<int> height = {4, 3, 2, -1, 4};


    int i=0, j=height.size()-1;
    int maxArea=0;

    if(! checkTestcase(height)){
        cout<<"Invalid Testcase"<<endl;
        return 0;
    }

    while(i<j){
        int area = min(height[i],height[j]) * (j-i); //finding current area with min height
        if(height[i]>height[j]){
            j--; //moving away from the shorter tower to see if we can find a bigger tower
        }
        else{
            i++;
        }
        maxArea=max(area,maxArea);
    }
    cout<<maxArea;


    return 0;
}

bool checkTestcase(vector<int> arr){

    for(int i=0; i<arr.size(); i++){
        if(arr[i]<0){
            return false;
        }
    }
    
    return true;
}
