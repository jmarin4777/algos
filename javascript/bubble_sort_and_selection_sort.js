function bubble_sort(arr){
    for(var i=0; i<arr.length-1; i++){
        var swapped = false
        for(var j=0; j<arr.length-1-i; j++){
            if(arr[j]>arr[j+1]){
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                swapped = true
            }
        }
        if(swapped==false){
            break
        }
    }
}
x = [6,5,3,1,8,7,2,4]
bubble_sort(x)
console.log(x)

function selectionSort(arr){
    // find the min value and swap it to the first index
    // move forward in the array and continue the loop.
    for(var i=0; i<arr.length; i++){
        var min = i
        for(var j=i; j<arr.length; j++){
            if(arr[j] < arr[min]){
                min = j
            }
        }
        var temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    }
}
x = [6,5,3,1,8,7,2,4]
selectionSort(x)
console.log(x)