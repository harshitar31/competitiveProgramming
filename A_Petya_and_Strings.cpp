#include <iostream>
#include <cctype>

int main(){

    std::string str1,str2;
    std::cin>>str1;
    std::cin>>str2;

    for (int i = 0; i < str1.length(); i++) {
        str1[i] = std::tolower(str1[i]);
    }

    for (int i = 0; i < str2.length(); i++) {
        str2[i] = std::tolower(str2[i]);
    }

    std::cout<<str1.compare(str2);

    return 0;
}