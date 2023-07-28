#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
    //双指针右指针 
    // right
    // right 指向当前将要处理的元素，左指针 
    // left
    // left 指向下一个将要赋值的位置。
        int l=0,n = nums.size();
        for(int r=0;r<n;r++){
            if(nums[r]!=val){
                nums[l]=nums[r];
                l++;
            }
        }
        return l;
    }
};