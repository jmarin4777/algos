[1,2,3,4,5,1,2,1,2]
function loops(head){
    var runner = head
    var runner2 = head
    while(runner != null){
        if(runner===runner2){
            return true
        }
        runner = runner.next
        runner2 = runner2.next.next
    }
    return false
}

function loops_break(head){
    var runner = head
    var runner2 = head
    var count = 0
    while(runner != null){
        if(runner===runner2){
            break
            }
        runner = runner.next
        runner2 = runner2.next.next
        count++
    }
    if(runner == null){
        return false
    }
    moves = 0
    runner = head
    while(runner != null){
        while(moves < count){
            // identifies when runner1 hits the beginning of the loop
            if(runner===runner2){
                var beginning = runner
                break
            }
            runner2 = runner2.next
            moves++
        }
        moves = 0
        runner = runner.next
    }
    // iterates runner2 until the next value is the beginning of the loop identified above
    while(runner2 != null){
        if(runner2.next === beginning){
            runner2.next = null
            return head
        }
        runner2 = runner2.next
    }
}