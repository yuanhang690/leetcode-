#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        // for(int i=0;i<nums.size();i++){
        //     // int j=i+1;//坑，可能会越界访问
        //     if (i==nums.size()-1)
        //     {
        //         break;
        //     }
            
        //     if(nums[i]==nums[j]){
        //         return true;
        //     }else{
        //         j++;
        //         if(j==nums.size())
        //             continue;
        //     }
            
        // }
        // return false;
        set<int> a(nums.begin(),nums.end());
        if (a.size()!=nums.size())
        {
            return true;
        }else{
            return false;
        }
        
    }
};
int main(){
    Solution Solution;
    vector<int> nums = {1,2,3,1};
    cout<<Solution.containsDuplicate(nums)<<endl;
    return 0;
}