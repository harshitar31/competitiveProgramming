#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

vector<pair<int,string>> roundRobin (vector<tuple<string, int, int, int>> processes, int quantum);
int count(vector<tuple<string, int, int, int>> arr,int num);
int contextSwitch(vector<pair<int,string>> schedule);

int main(){

    vector<tuple<string, int, int, int>> processes;
    //Process Arrival Burst Priorities
    processes = {{"P1", 0, 20, 2},{"P2", 15, 25, 4}, {"P3", 30, 10, 1}, {"P4", 45, 15, 3}};
    int quantum=2;

    vector<pair<int,string>> rr; 
    rr = roundRobin(processes, quantum);
    for (const auto& pair:rr){
        cout<<pair.first<<" "<<pair.second<<endl;
    }

    int rrCount = contextSwitch(rr);
    cout<<"Context Switches: "<<rrCount<<endl;



    return 0;
}

vector<pair<int,string>> roundRobin (vector<tuple<string, int, int, int>> processes, int quantum){
    vector<pair<int,string>> schedule;
    int time=0;
    int p=0;
    while(count(processes,0) != (int) processes.size()){
        if(get<1>(processes[p])<=time and get<2>(processes[p])>0){
            schedule.push_back({time,get<0>(processes[p])});
            if (get<2>(processes[p])<quantum){
                time+=get<2>(processes[p]);
                get<2>(processes[p])=0;
            }
            else{
                get<2>(processes[p])-=quantum;
                time+=quantum;
            }
        }
        p=(p+1)%processes.size();
    }
    return schedule;
}

int count(vector<tuple<string, int, int, int>> arr,int num){
    int c=0;
    for(const auto& i:arr){
        if(get<2>(i)==num){
            c++;
        }
    }
    return c;
}

int contextSwitch(vector<pair<int,string>> schedule){
    int count=1;
    string prev=schedule[0].second;
    for(const auto& pair: schedule){
        if(pair.second!=prev){
            count++;
            prev=pair.second;
        }
    }
    return count;
}