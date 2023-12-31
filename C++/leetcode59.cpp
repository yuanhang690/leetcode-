#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution
{
public:
    vector<vector<int>> generateMatrix(int n)
    {
        vector<vector<int>> matrix(n);
        for (int i = 0; i < matrix.size(); i++)
            matrix[i].resize(n);
        // 上下左右
        int u = 0;
        int d = n - 1;
        int l = 0;
        int r = n - 1;
        int num = 1;

        while (true)
        {
            // 上
            for (int i = l; i <= r; i++)
                matrix[u][i] = num++;
            if (u++ >= d)
                break;
            // 右
            for (int i = u; i <= d; i++)
                matrix[i][r] = num++;
            if (r-- <= l)
                break;
            // 下
            for (int i = r; i >= l; i--)
                matrix[d][i] = num++;
            if (d-- <= u)
                break;
            // 左
            for (int i = d; i >= u; i--)
                matrix[i][l] = num++;
            if (l++ >= r)
                break;
        }
        return matrix;
    }
};

int main()
{
    Solution solution;
    int n = 3;
    vector<vector<int>> ans = solution.generateMatrix(n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}