// list = 
// [1]<-[5]->[8]->[3]->[9]


function reverse(list){
    runner = list.head
    next = 0
    while(runner != null){
        follower = runner
        if(next == null){
            list.head = runner
            break
        }
        if(runner != list.head){
            runner = next
            next = runner.next
        }
        else{
            next = runner.next.next
            runner = runner.next
            follower.next = null
        }
        
        runner.next = follower
        
    }
}