/*
cho mot list vi du nhu a1->a2->a3->...->a(2n)
print a1->a3->...->a(2n-1)->a2->a4->...->a(2n)
*/

/*
tao ra 2 list a1->...->a(2n-1) vaf a2->...->a(2n) roi merge 
neu tao rieng re tung list thi se bi lost link between giua 2 phan tu lien tiep
--> tao 2 list dong thoi
*/
#include <iostream>
#include <vector>
using namespace std;
 
// A Linked List Node
struct Node
{
    int data;
    Node* next;
};
 
// Helper function to print a given linked list
void printList(Node* head)
{
    Node* ptr = head;
    while (ptr)
    {
        cout << ptr->data << " —> ";
        ptr = ptr->next;
    }
 
    cout << "null\n";
}
 
// Helper function to insert a new node at the beginning of the linked list
void push(Node** headRef, int data)
{
    Node* newNode = new Node();
    newNode->data = data;
    newNode->next = *headRef;
 
    *headRef = newNode;
}
 
// Function to rearrange the linked list in a specific manner
void rearrange(Node* head)
{
    // empty list or one node
    if (head == nullptr || head->next == nullptr) {
        return;
    }
 
    // create two dummy nodes
    Node dummyFirst, dummySecond;
 
    // tail pointer for the first and second list
    Node* first = &dummyFirst, *second = &dummySecond;
 
    Node* curr = head;
 
    // iterate through the list and process two nodes at a time
    while (curr != nullptr)
    {
        // move the current node to the first list
        first->next = curr;
        first = first->next;
 
        // move the next node to the second list
        if (curr->next != nullptr)
        {
            second->next = curr->next;
            second = second->next;
            curr = curr->next;
        }
        curr = curr->next;
    }
 
    // combine the first list with the second list
    first->next = dummySecond.next;
    second->next = nullptr;
}
 
int main()
{
    // input keys
    vector<int> keys = { 1, 2, 3, 4, 5 };
 
    Node* head = nullptr;
    for (int i = keys.size() - 1; i >= 0; i--) {
        push(&head, keys[i]);
    }
 
    rearrange(head);
    printList(head);
 
    return 0;
}
