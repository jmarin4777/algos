function removeVal(node, val){
    var val_to_remove = val
    var runner = node
    var count = 0
    if(node.val == val_to_remove){
        node = node.next
    }
    while(runner != null){
        if(runner.next.val == val_to_remove){
            runner.next = runner.next.next
            count ++
        }
        runner = runner.next
    }
    if(count == 0){
        return "Value not found"
    }
    return node
}