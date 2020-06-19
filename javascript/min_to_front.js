function min_to_front(head){
    var min = head;
    var runner = head;
    var temp = head;
    while(runner != null){
        if(min.val > runner.val){
            min = runner;
        }
        runner = runner.next;
    }
    var runner = head;
    while(runner != null){
        if(runner.next == min){
            temp = min.next;
            min.next = head;
            runner.next = temp;
        }
    }
}

function move_max_to_back(head){
    var max = head;
    var runner = head;
    while(runner != null){
        if(max<runner.val){
            max = runner;
        }
        if(runner.next == null){
            runner.next = max;
            // max = null;
        }
        runner = runner.next
    }

}
[10] [2] [1] [4] [5]
