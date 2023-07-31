/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;#include <iostream>
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



class Solution{
public:
    ListNode *removeElements(ListNode *head, int val)
    {
        struct ListNode* dummpny = new ListNode(0,head);
        struct ListNode* p = head;
        while(p->next!=NULL){
            if(p->next->val==val){
                struct ListNode* temp = p->next;
                p->next=p->next->next;
                delete temp;
            }else{
                p = p->next;
            }
        }
        return dummpny->next;
    }
};