function full(root){
    if(root.left == null && root.right == null){
        return true
    }

    if(root.left != null && root.right != null){
        return full(root.left) && full(root.right)
    }

    return false
}

function complete(root){

}


//         4
//     2       7
// 1      3 6
