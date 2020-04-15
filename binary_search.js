x = [1,2,3,4,5,6,7,8,9,10]
val = 9
function binsearch(arr,val){
    x = arr.length
    y = Math.floor(x/2)
    if (arr.length == 1){
        return console.log("The value is not in the array")
    }
    if (val == arr[y]){
        return console.log("The value is in the array")
    } else if(val > arr[y]){
        arr.splice(0, y)
    } else if (val < arr[y]){
        arr.splice(y, x-y)
    }
    return binsearch(arr, val)
}
binsearch(x,val)