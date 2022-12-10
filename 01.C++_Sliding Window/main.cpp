#include <iostream>
#include <vector>
#include "Solution.h"
using namespace std;



int main() {
    vector<int> something;
    something.push_back(1);
    something.push_back(1);
    something.push_back(2);
    something.push_back(2);
    something.push_back(2);
    something.push_back(3);
    something.push_back(3);
    something.push_back(4);
    something.push_back(5);
    vector<int>& go=something;
    Solution sol;
    sol.removeDuplicates(go);
    for (int i=0; i<something.size(); i++){
        cout<<i<<": "<<something.at(i)<<endl;
    }

    return 0;
}
