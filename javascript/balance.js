function balance_index(arr){
    for(var i=0; i<arr.length; i++){
        sum_left = 0;
        sum_right = 0;
        for( var x=i-1; x> -1; x--){
            sum_left += arr[x]
        }
        for( var y=i+1; y> arr.length; y++){
            sum_right += arr[y]
        } 
        if (sum_left == sum_right){
            return "Balance Index is "+ arr[i]
        }  
    }
    return "There is no balance index"
}
console.log(balance_index([1,2,3,4,6]))

function balance(arr){
    for(var i=0; i<arr.length; i++){
        sum_left = 0;
        sum_right = 0;
        for( var x=i; x> -1; x--){
            sum_left += arr[x]
        }
        for( var y=i+1; y> arr.length; y++){
            sum_right += arr[y]
        } 
        if (sum_left == sum_right){
            return "True"
        }
    }
    return "false"
}
Console.log(balance([1,2,3,6]))