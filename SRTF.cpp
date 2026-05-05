#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

bool compareArrival(tuple<string, int, int, int> processA, tuple<string, int, int, int> processB);
bool compareBurstTime(tuple<string, int, int, int> processA, tuple<string, int, int, int> processB);
vector<pair<int,string>> SRTF(vector<tuple<string, int, int, int>> processes);



int main(){

    vector<tuple<string, int, int, int>> processes;
    //Process Arrival Burst Priorities
    processes = {{"P1", 0, 20, 2},{"P2", 15, 25, 4}, {"P3", 30, 10, 1}, {"P4", 45, 15, 3}};


    vector<pair<int,string>> srtf; 
    srtf = SRTF(processes);
    for (const auto& pair:srtf){
        cout<<pair.first<<" "<<pair.second<<endl;
    }





    return 0;
}

bool compareArrival(tuple<string, int, int, int> processA, tuple<string, int, int, int> processB) {
    return get<1>(processA) < get<1>(processB); 
}

bool compareBurstTime(tuple<string, int, int, int> processA, tuple<string, int, int, int> processB) {
    return get<2>(processA) < get<2>(processB); 
}

vector<pair<int,string>> SRTF(vector<tuple<string, int, int, int>> processes){
    vector<pair<int,string>> schedule={};
    sort(processes.begin(),processes.end(),compareArrival);
    int time = 0;
    int completed = 0; 
    int n = processes.size();

    vector<bool> isCompleted(n, false);

    
    while(completed<n){
        vector<tuple<string, int, int, int>> readyQueue;
        for(int i=0;i<n;i++){
            if(!isCompleted[i] && get<1>(processes[i])<=time){
                readyQueue.push_back(processes[i]);
            }
        }

        if(!readyQueue.empty()){
            sort(readyQueue.begin(), readyQueue.end(), compareBurstTime);

            schedule.push_back({time, get<0>(readyQueue[0])});

            int processIndex = distance(processes.begin(),find(processes.begin(), processes.end(), readyQueue[0]));
            get<2>(processes[processIndex])--;


            if (get<2>(processes[processIndex])== 0) {
                isCompleted[processIndex] = true;
                completed++;
            }
            time++;
        }
        else{
            time++;
        }
    }
    return schedule;
  
  }
  