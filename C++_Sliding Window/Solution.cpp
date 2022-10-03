//
// Created by 태윤 on 2022-01-27.
//

#include <vector>
#include <iostream>
using namespace std;
#include "Solution.h"

    int removeDuplicates(vector<int>& nums)
    {
        vector<int> tmp;
        tmp.push_back(nums.at(0));
        for(int i=0; i<nums.size()-1; i++){
            int val=i+1;
            if(nums.at(i)!=nums.at(val)){
                tmp.push_back(nums.at(val));
            }
        }

        nums.clear();
        for(int i=0; i<tmp.size(); i++){
            nums.push_back(tmp.at(i));
        }

        return 0;
    }
