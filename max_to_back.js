function max_to_back(head){
    var max = head;
    var runner = head;
    while(runner != null){
        if (max.val < runner.val){
            max = runner;
        }
        runner  = runner.next
    }
    runner = head
    while(runner != null){
        if(runner.next == max){
            runner.next = runner.next.next;
        }
        if(runner.next == null){
            runner.next = max;
            max.next = null;
            return head
        }
        runner = runner.next
    }
}