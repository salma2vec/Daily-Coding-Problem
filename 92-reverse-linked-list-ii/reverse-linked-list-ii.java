/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
         if(m==n) return head;
 
    ListNode prev = null;
    ListNode one = new ListNode(0);
    ListNode two = new ListNode(0); 
    int i=0;
    ListNode p = head;
    while(p!=null){
        i++;
        if(i==m-1){
            prev = p;
        }
 
        if(i==m){
            one.next = p;
        }
 
        if(i==n){
            two.next = p.next;
            p.next = null;
        }
 
        p= p.next;
    }
    if(one.next == null)
        return head;
 
    // reverse list [m, n]    
    ListNode a = one.next;
    ListNode b = a.next;
    a.next = two.next;
 
    while(a!=null && b!=null){
        ListNode c = b.next;
        b.next = a;
        a = b;
        b = c;
    }
 

    if(prev!=null)
        prev.next = a;
    else
        return a;
 
    return head;
 }
        
}