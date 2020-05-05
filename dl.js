function DLList(){
    this.head = null
    this.tail = null

    this.push = function(node, dlist=this){
        dlist.tail.next = node
        node.prev = dlist.tail
        dlist.tail = node
        return dlist
    }

    this.pop = function(){
        result = this.tail
        this.tail = this.tail.prev
        this.tail.next = null
        result.prev = null
        return result

    }
    function prepend(newval, oldval){
        var runner = this.head
        
        while(runner != null){
            if(oldval == runner.val){
                temp = runner.prev
                newNode = new DLNode(newval)
                newNode.next = runner
                newNode.prev = temp
                temp.next = newNode
                runner.prev = newNode
            }
            runner = runner.next
        }
    }
    function append(newval, oldval){
        var runner = this.head
        
        while(runner != null){
            if(oldval == runner.val){
                temp = runner.next
                newNode = new DLNode(newval)
                newNode.next = temp
                newNode.prev = runner
                temp.prev = newNode
                runner.next = newNode
            }
            runner = runner.next
        }
    }
    function delete_middle(node){
        var runner = this.head
        var length = 0
        while(runner != null){

            length++
            runner = runner.next
        }
    }
}
function DLNode(val){
    this.val = val
    this.prev = null
    this.next = null
}
x = new DLList()
x.push(new DLNode(1))
x.push(new DLNode(2))
x.push(new DLNode(3))
x.push(new DLNode(4))
x.push(new DLNode(5))
x.prepend(7,3)
console.log(x)


// var a = new slnode('a')
// var b = new slnode('b')
// var c = new slnode('c')
// var d = new slnode('d')
// var e = new slnode('e')
// var f = new slnode('f')
// var g = new slnode('g')
// var h = new slnode('h')
// var i = new slnode('i')
// var j = new slnode('j')

// a.next = b
// b.next = c
// c.next = d

// e.next = f
// f.next = g

// h.next = i
// i.next = j
