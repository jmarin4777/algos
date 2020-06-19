function insertionSort(arr){
    for (var i = 1; i < arr.length; i++){
        var j = i - 1;
        var val = arr[i];
        while ( j >= 0 && val < arr[j]){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = val;
    }
    return console.log(arr);
}
insertionSort([5,3,9,6,8,7])
// Time: O(n^2) Space: O(1)