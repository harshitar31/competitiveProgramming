// https://codeforces.com/problemset/problem/282/A

#include <iostream>

int main(){

    int n;
    std::cin>>n;
    int x=0;
    std::string input;
    while(n--){
        std::cin>>input;
        char op = input.at(1);
        switch (op){
            case '+':
            x++;
            break;
            case '-':
            x--;
            break;
        }
    }
    std::cout<<x;

    return 0;
}
