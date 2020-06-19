// 5 after 10

function appendVal(node, val, after){
    var runner = node;
    var nuNode = NewNode(val);
    var count = 0;
    while(runner != null){
        if(runner.val == after){
            temp = runner.next;
            runner.next = nuNode;
            nuNode.next = temp;
            count ++;
        }
        runner = runner.next;
    }
    if(count == 0){
        runner = node;
        while(runner != null){
            if(runner.next == null){
                runner.next = nuNode
                return node
            }
            runner = runner.next
        }
    }
    return node
}