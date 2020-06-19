// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example:

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.

// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
var l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
var l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

var addTwoNumbers = function(l1, l2) {
    var l3, runner1 = l1, runner2 = l2, runner3, sum;
    
    while(runner1 != null || runner2 != null){
        var num1 = 0, num2 = 0;
        if(runner1 != null){
            num1 = runner1.val;
        }
        if(runner2 != null){
            num2 = runner2.val;
        }
        
        sum = num1 + num2;
        if(l3){
            if(runner3.next){
                sum += 1;
            }
            if(sum >= 10){
                runner3.next = new ListNode(sum-10, new ListNode(1));
            } else{
                runner3.next = new ListNode(sum);
            }   
            runner3 = runner3.next;
        } else{
            if(sum >= 10){
                l3 = new ListNode(sum-10, 1);
            } else{
                l3 = new ListNode(sum);
            }   
            runner3 = l3;
        }
        
        if(runner1 != null){
            runner1 = runner1.next;
        }
        if(runner2 != null){
            runner2 = runner2.next;
        }
    }
    return l3
};
console.log(addTwoNumbers(l1, l2));