// SList: Priority Queue
// We want to create a Queue data structure that keeps its elements in sorted order, so that when we call pop(), we get the first element in sorted order (rather than sequential order, like a regular FIFO queue). 
// Create a PriQueue data structure by making changes tl SLQueue and SLNode. A PriQNode class should be identical to SLNode, plus .pri, which is set by an additional argument passed to the constructor.The PriQueuepush() method should accept both value and priority, and priority should be used to add the node at the right spot (instead of at queue's end).

function priQNode(val, pri){
    this.val = val;
    this.pri = pri;
    this.next = null;
}

function priQueue(){
    this.head = null;

    this.enqueue = function(node){
        //add a node in pri order
        //3 -> 4 -> 7 -> 9
        //push(5)
        // 3 -> 4 -> 5 -> 7 -> 9
        if(this.head == null){
            this.head = node;
            return this.head;
        }
        var runner = this.head;
        while(runner != null){
            if(node.pri < runner.next.pri){
                node.next = runner.next;
                runner.next = node;
                return this.head;
            }
            if(runner.next == null){
                runner.next = node;
                return this.head;
            }
            runner = runner.next;
        }
    }

    this.dequeue = function(){
        //returns head and removes it
        var runner = this.head;
        this.head = runner.next;
        runner.next = null;
        return runner;
    }
}
