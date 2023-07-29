/*
209. 长度最小的子数组
https://leetcode.cn/problems/minimum-size-subarray-sum/



*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution
{
public:
    int minSubArrayLen(int target, vector<int> &nums)
    { // 暴力求解
        //  if(nums.size()==0)
        //      return 0;
        //  int ans = INT_MAX;
        //  int n = nums.size();
        //  for (int i = 0; i < n;i++){
        //      int sum = 0;
        //      for (int j = i; j < n;j++){
        //          sum += nums[j];
        //          if(sum>=target){
        //              ans = min(ans, j-i+1);
        //              break;
        //          }
        //      }
        //  }
        //  return ans == INT_MAX ? 0 : ans;
        // 方法二：滑动窗口(解析)
        // https://leetcode.cn/problems/minimum-size-subarray-sum/solution/javade-jie-fa-ji-bai-liao-9985de-yong-hu-by-sdwwld/
        //
        int n = nums.size();
        int start = 0, end = 0, sum = 0, ans = INT_MAX;
        while (end < n)
        {
            sum += nums[end];
            while (sum >= target)
            {
                ans = min(ans, end - start + 1);
                sum -= nums[start];
                start++;
            }
            end++;
        }
        return ans == INT_MAX ? 0 : ans;
    }
};
