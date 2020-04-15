// [1,2,3,4,10] -> true
function balance_point(arr){
    var sum1 = 0
    var sum2 = 0
    x = arr.length-1
    for(var i=0;i<x;i++){
        sum1 = sum1 + arr[i]
        for(var j=x;j>i;j--){
            sum2 = sum2 + arr[j]
        }
        if(sum1==sum2){
            return true
        }
        sum2 = 0
    }
    return false
}
x = [1,2,3,4,10]
console.log(balance_point(x))

// [-2,5,7,0,3] -> 2
function balance_index(arr){
    var sum1 = 0
    var sum2 = 0
    x = arr.length-1
    for(var i=0;i<x;i++){
        sum1 = sum1 + arr[i]
        for(var j=x;j>i;j--){
            sum2 = sum2 + arr[j]
        }
        if(sum1==sum2){
            return true
        }
        sum2 = 0
    }
    return false
}
x = [-2,5,7,0,3]
console.log(balance_index(x))