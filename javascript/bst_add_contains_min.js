function BTNode(value){
    this.val = value;
    this.left = null;
    this.right = null;
}

function BST(){
    this.root = null;

    function add(value){
        runner = this.root
        new_node = new BTNode(value)
        while(runner != null){
            if(new_node.val < runner.val){
                if(runner.left == null){
                    runner.left = new_node
                    return this.root
                }
                else{
                    runner = runner.left
                }
            }
            else if(new_node.val > runner.val){
                if(runner.right == null){
                    runner.right = new_node
                    return this.root
                }
                else{
                    runner = runner.right
                }
            }
            else if(new_node.val == runner.val){
                temp_left = runner.left
                temp_right = runner.right
                runner.right = null
                runner.left = new_node
                new_node.left = temp_left
                new_node.right = temp_right
                return this.root
            }
        }
    }

    function contains(value){
        runner = this.root
        while(runner != null){
            if(value == runner.val){
                return 'The value is in the binary search tree'
            }
            else if(value > runner.val){
                if(runner.right){
                    runner = runner.right
                }
                else{
                    return 'The value is not in the binary search tree'
                }
            }
            else if(value < runner.val){
                if(runner.left){
                    runner = runner.left
                }
                else{
                    return 'The value is not in the binary search tree'
                }
            }
        }
    }

    function min(){
        runner = this.root
        while(runner != null){
            if(runner.left == null){
                return runner.val
            }
            else{
                runner = runner.left
            }
        }
    }
}