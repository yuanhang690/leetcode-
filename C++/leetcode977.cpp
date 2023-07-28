/*
977. 有序数组的平方
https://leetcode.cn/problems/squares-of-a-sorted-array/
方法二思路：
使用两个指针分别指向位置0 和n-1
每次比较两个指针对应的数,选择较大的那个逆序放入答案并移动指针
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        // int n=nums.size();
        // for(int i=0;i<n;i++){
        //     int temp = nums[i];
        //     nums[i] = temp*temp;
        // }
        // sort(nums.begin(),nums.end());
        // return nums;
        // 方法二：
        int n = nums.size();
        vector<int> ans(n);
        for (int i = 0, j = n - 1, pos = n - 1; i <= j;)
        {
            if (nums[i] * nums[i] > nums[j] * nums[j])
            {
                ans[pos] = nums[i] * nums[i];
                i++;
            }
            else
            {
                ans[pos] = nums[j] * nums[j];
                j--;
            }
            pos--;
        }
        return ans;
    }
};