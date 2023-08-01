#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class MyLinkedList {
public:
    //定义结点结构
    struct LinkedNode{
        int val;
        LinkedNode* next;
        LinkedNode(int val):val(val),next(nullptr){}
    };
    LinkedNode* _dummyhead;
    //使用一个变量来记录链表长度
    int _size;


    MyLinkedList() {
        _dummyhead = new LinkedNode(0);
        _size = 0;
    }
    
    int get(int index) {
        //注
        if(index>=_size)
            return -1;
        LinkedNode* cur = _dummyhead;
        int i=0;
        while(i<=index){
            cur = cur->next;
            i++;
        }
        return cur->val;
    }
    
    void addAtHead(int val) {
        LinkedNode* p = new LinkedNode(val);
        p->next = _dummyhead->next;
        _dummyhead->next = p;
        _size++;
    }
    
    void addAtTail(int val) {
        LinkedNode* p = new LinkedNode(val);
        LinkedNode* cur = _dummyhead;
        while(cur->next!=NULL){
            cur = cur->next;
        }
        cur->next = p;
        _size++;
    }
    
    void addAtIndex(int index, int val) {
        //注
        if(index>_size)
            return;
        LinkedNode* cur = _dummyhead;
        while(index--){
            cur = cur->next;
        }
        LinkedNode* p = new LinkedNode(val);
        p->next = cur->next;
        cur->next = p;
        _size++;
    }
    
    void deleteAtIndex(int index) {
        //注
        if(index>=_size)
            return;


        LinkedNode* cur = _dummyhead;
        // 注
        while(index--){
            cur = cur->next;
        }
        LinkedNode* temp = cur->next;
        cur->next = cur->next->next;
        delete temp;

        //注
        _size--;
    }
};