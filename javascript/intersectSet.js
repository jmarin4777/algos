function intersect (arr1, arr2) {
    var newarr = [];
    let dict = {};
    for(i = 0; i < arr1.length; i ++){
        if(dict[arr1[i]]){
            dict[arr1[i]] += 1;
        } else{
            dict[arr1[i]] = 1;
        }
    }
    for(j = 0; j < arr2.length; j++){
        if(dict[arr2[j]] > 0){
            dict[arr2[j]] -= 1;
            newarr.push(arr2[j]);
        }
    }
    console.log(newarr);
    return newarr
}
intersect([1,2,2,2,7], [2,2,6,6,7])

function union(arr1,arr2){
        let x = 0;
        let y = 0;
        var newArr = []
        while(x != arr1.length || y != arr2.length){
            if(arr1[x] < arr2[y]){
                newArr.push(arr1[x])
                x++
            }else if(arr2[y] < arr1[x]){
                newArr.push(arr2[y])
                y++
            }else{
                newArr.push(arr1[x])
                x++
                y++
            }
            
        }
        return newArr
    }
    console.log(union([1,2,2,2,7], [2,2,6,6,7])) 

function intersectInPlace(arr1, arr2){
    for(var i=0; i<arr1.length; i++){
        var swapped = false;
        for(var j=0; j<arr2.length; j++){
            if(arr2[j]==arr1[i]){
                let temp = arr2[j];
                arr2[j] = arr2[arr2.length-1];
                arr2[arr2.length-1] = temp;
                arr2.pop();
                swapped = true;
                break
            }
        }
        if(swapped == false){
            let temp = arr1[i];
            arr1[i] = arr1[arr1.length-1];
            arr1[arr1.length-1] = temp;
            arr1.pop();
            i--;
        }
    }
    console.log(arr1);
    return arr1
}
intersectInPlace([2,7,2,1,2], [6,7,2,7,6,2])