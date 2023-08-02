/*



*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        //定义虚拟头结点，方便后面删除操作
        ListNode* dummyhead = new ListNode(0);
        dummyhead->next = head;
        ListNode* cur = dummyhead;
        while(cur->next!=nullptr&&cur->next->next!=nullptr){
            ListNode* pre = cur->next;
            ListNode* next = cur->next->next;
            cur->next = next;
            pre->next = next->next;
            next->next = pre;
            cur = cur->next->next;
        }
        return dummyhead->next;
    }
};